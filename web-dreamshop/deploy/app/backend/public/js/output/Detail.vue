<!-- Detail.vue (route "detail", path "/:id/detail") -->
<!-- reconstructed from render fn `k` / component `$` in app_9ada4703.js -->
<template>
  <div class="detail">
    <b-form @submit="onSubmit">
      <img :src="item.poster" style="width: 500px" />
      <br />
      <h1>{{ item.name }}</h1>
      <section>
        <p>가격: ${{ item.price }}</p>
        <!-- item.detail is injected as raw HTML (v-html). It is passed
             through DOMPurify below before being assigned. -->
        <p v-html="item.detail"></p>
      </section>
      <b-button variant="success" type="submit">Buy</b-button>
      <router-link class="link" :to="{ name: 'index' }">
        <b-button>Back</b-button>
      </router-link>
    </b-form>
  </div>
</template>

<script>
// NB: in the bundle these are webpack requires resolved at runtime:
//   createDOMPurify = require("dompurify")   // module c0c4
//   { JSDOM }       = require("jsdom")        // module 7a7a (browserified)
import createDOMPurify from "dompurify";
import { JSDOM } from "jsdom";

export default {
  data() {
    return { item: this.item };
  },
  created() {
    this.id = this.$route.params.id;
    this.item = [];

    this.$http
      .get(`/${this.id}/info`)
      .then((res) => {
        this.item = res.data;

        // Client-side sanitization: a DOMPurify instance is built on top of
        // a fresh JSDOM window (jsdom bundled into the browser build), then
        // used to clean the server-supplied HTML before v-html renders it.
        const window = new JSDOM("").window;
        const DOMPurify = createDOMPurify(window);
        this.item.detail = DOMPurify.sanitize(this.item.detail);
      })
      .catch(() => {
        location.href = "/";
      });
  },
  methods: {
    onSubmit(e) {
      e.preventDefault();
      this.$http
        .post(`/${this.id}/buy`)
        .then((res) => {
          this.$cookie.set("token", res.data.token);
          alert("buy item!");
          location.href = res.data.data; // server-provided redirect target
        })
        .catch((err) => {
          alert(err.response.data);
        });
    },
  },
};
</script>
