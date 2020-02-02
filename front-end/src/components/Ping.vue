<template>
  <div class="container">
    <button type="button" class="btn btn-primary">{{ msg }}</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Ping",
  data: function() {
    return {
      msg: ""
    };
  },
  methods: {
    getMessage: function() {
      const path = "http://127.0.0.1:5000/api/ping";
      axios
        .get(path)
        .then(res => {
          this.msg = res.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  },

  created() {
    this.getMessage();
  }
};
</script>

<style>
</style>