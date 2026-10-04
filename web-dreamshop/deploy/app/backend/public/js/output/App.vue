<!-- App.vue — reconstructed from render fn `r` / component `a` in app_9ada4703.js -->
<template>
  <div id="app">
    <b-navbar class="nav" type="dark" variant="dark">
      <b-navbar-nav>
        <router-link :to="{ name: 'index' }">
          <b-navbar-item>Home</b-navbar-item>
        </router-link>
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto">
        <router-link :to="{ name: 'report' }">
          <b-navbar-item>Report</b-navbar-item>
        </router-link>

        <!-- Logged in: show Logout. Otherwise: show Login link. -->
        <b-navbar-item v-if="info">
          <!-- clears the token cookie, then reloads the current page -->
          <a href="javascript:document.cookie='token=';location.href=''">Logout</a>
        </b-navbar-item>
        <router-link v-else :to="{ name: 'login' }">
          <b-navbar-item>Login</b-navbar-item>
        </router-link>
      </b-navbar-nav>
    </b-navbar>

    <div class="main">
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  name: "app",
  data() {
    return { info: this.info };
  },
  created() {
    // Probe whether the session is authenticated.
    this.$http
      .get("/user/info")
      .then(() => {
        this.info = true;
      })
      .catch(() => {
        this.$cookie.delete("token");
      });
  },
};
</script>
