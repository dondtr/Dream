<!-- Login.vue (route "login", path "/login/") -->
<!-- reconstructed from render fn `S` / component `P` in app_9ada4703.js -->
<template>
  <div>
    <b-form @submit="onSubmit">
      <b-form-group id="input-group-1" label="id" label-for="input-1">
        <b-form-input
          id="uid"
          type="text"
          required
          placeholder="Enter user id"
          v-model="form.uid"
        />
      </b-form-group>

      <b-form-group id="input-group-2" label="pw" label-for="input-2">
        <b-form-input
          id="upw"
          type="password"
          required
          placeholder="Enter user pw"
          v-model="form.upw"
        />
      </b-form-group>

      <b-button type="submit" variant="primary">Login</b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  data() {
    return { form: { uid: "", upw: "" } };
  },
  created() {
    // login() is deliberately exposed on the global window object.
    window.login = this.login;
  },
  methods: {
    onSubmit(e) {
      e.preventDefault();
      this.login(this.form);
    },
    login(form) {
      this.$http
        .post("/login", form)
        .then((res) => {
          this.$cookie.set("token", res.data.token);
          location.href = "/";
        })
        .catch((err) => {
          alert(err.response.data);
        });
    },
  },
};
</script>
