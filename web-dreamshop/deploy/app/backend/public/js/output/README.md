# Deobfuscation of `app_9ada4703.js` + `chunk-vendors_30de09e7.js`

Both inputs are **webpack 4 production bundles** of a **Vue 2.6.11** single-page
app (BootstrapVue UI). `app.*` is the application code; `chunk-vendors.*` is the
third-party dependency chunk.

## What's in this folder

| File | What it is |
| --- | --- |
| `app.beautified.js` | `app_9ada4703.js` mechanically re-indented (js-beautify). Still webpack module format, single-letter vars. |
| `chunk-vendors.beautified.js` | `chunk-vendors_30de09e7.js` re-indented. ~31.7k lines / 5.2 MB of bundled npm libraries. |
| `app.reconstructed/` | The application rebuilt into readable Vue single-file components. **This is the real "human-readable" version.** |

The app bundle had already been run through a formatter once (it shipped with
newlines), so the interesting work is `app.reconstructed/`.

## `app.reconstructed/` layout

```
main.js            # Vue init, router, axios instance + request interceptor (module 56d7)
App.vue            # navbar shell + auth probe        (render fn r / component a)
views/
  Home.vue         # route "index"  /                 (render fn h / component v)
  Detail.vue       # route "detail" /:id/detail       (render fn k / component $)
  Login.vue        # route "login"  /login/           (render fn S / component P)
  Report.vue       # route "report" /report           (render fn q / component T)
```

Webpack render functions (`n("tag", {attrs}, [children])`) were translated back
into template markup. Each file notes the original minified symbol it came from.

## Routes / API surface

| Route | Path | Calls |
| --- | --- | --- |
| index  | `/`             | `GET /items`, `GET /user/info` |
| detail | `/:id/detail`   | `GET /:id/info`, `POST /:id/buy` |
| login  | `/login/`       | `POST /login` |
| report | `/report`       | `POST /report` |

Auth is a `token` cookie, re-attached to every request as a `token` header by
the axios interceptor in `main.js`.

## Vendor chunk (`chunk-vendors`) — module manifest

583 webpack modules (4-hex-char IDs). No source map shipped, so a full
ID→package map isn't recoverable, but the major libraries are identifiable by
fingerprint:

- **Vue.js 2.6.11** (`2b0e`)
- **vue-router** (`8c4f`)
- **BootstrapVue** (`5f5b`)
- **axios** (`bc3a`)
- **vue-cookie** (`00e7`)
- **DOMPurify** (`c0c4`)
- **jsdom** — browserified build (`7a7a`); pulls in **ajv**, and other Node-shim deps
- **core-js** polyfills

The vendor chunk is stock third-party code; beautifying is the ceiling there —
there's nothing app-specific to reconstruct.

## Security-relevant behavior (this reads like a CTF web target)

Purely from the code, not an assertion about intended use:

- `Detail.vue` renders `item.detail` via **`v-html`** (raw HTML injection). It's
  passed through **DOMPurify**, but sanitization runs **client-side** on a jsdom
  window — so it only holds if the server never renders `detail` itself and if
  the DOMPurify config/version has no bypass. This is the obvious XSS sink.
- `Report.vue` submits a URL path for the backend to fetch/visit — the classic
  **admin-bot** pattern (report a URL → bot with the privileged cookie opens it).
  Combined with the sink above, that's a cookie/`amount`-exfil XSS chain.
- The axios `".."` check is **client-side only** and trivially bypassed by
  hitting the API directly.
- `Login.vue` deliberately exposes `window.login`.
- `Detail.onSubmit` does `location.href = res.data.data` — an **open-redirect /
  navigation controlled by the server response**.

If you want, I can diff the DOMPurify version bytes in the vendor chunk against
known CVE-affected releases, or trace any specific module ID.
