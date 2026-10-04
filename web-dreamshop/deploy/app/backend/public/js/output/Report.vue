<!-- Report.vue (route "report", path "/report") -->
<!-- reconstructed from render fn `q` / component `T` in app_9ada4703.js -->
<template>
  <div>
    <b-form @submit="onSubmit">
      <b-form-group id="input-group-1" label="input url path" label-for="input-1">
        <div style="display: inline">
          <!-- shows the fixed origin prefix, e.g.  "http://host" + /yoururl -->
          <div v-text="host"></div>
          <b-form-input
            id="path"
            type="text"
            required
            placeholder="Enter url path"
            v-model="form.path"
          />
        </div>
      </b-form-group>

      <b-button type="submit" variant="primary">Submit</b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: { path: "" },
      host: '"' + new URL(location.href).origin + '" + /yoururl',
    };
  },
  methods: {
    onSubmit(e) {
      e.preventDefault();
      // Submits a path for the backend (an "admin bot") to visit.
      this.$http
        .post("/report", this.form)
        .then(() => {
          alert("report!");
          location.href = "/";
        })
        .catch((err) => {
          alert(err.response.data);
        });
    },
  },
};
</script>
