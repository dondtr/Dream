<!-- Home.vue (route "index", path "/") -->
<!-- reconstructed from render fn `h` / component `v` in app_9ada4703.js -->
<template>
  <div class="wrap">
    <!-- Greeting shown once /user/info returns the user object. -->
    <h1 v-if="info">Hello, {{ info.uid }} (${{ info.amount }})</h1>

    <ul class="items">
      <li v-for="item in items" :key="item.id" class="item">
        <router-link :to="{ name: 'detail', params: { id: item.id } }">
          <div class="detail" style="text-align: center">
            <img :src="item.poster" style="width: 250px" />
            <br />
            <strong class="name">{{ item.name }}</strong>
            <br />
            <span>가격 <span class="num">${{ item.price }}</span></span>
            <br />
          </div>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return { items: this.items, info: this.info };
  },
  created() {
    this.items = [];

    // Item catalogue.
    this.$http.get("/items").then((res) => {
      this.items = res.data;
    });

    // Current user (uid + amount). On failure, drop the token cookie.
    this.$http
      .get("/user/info")
      .then((res) => {
        this.info = res.data;
      })
      .catch(() => {
        this.$cookie.delete("token");
      });
  },
};
</script>
