<template>
  <form @submit.prevent="submitForm">
    <input id="url" placeholder="Recipe URL" type="text" v-model="formData.url" required />
    <br />
    <button type="submit">Submit</button>
  </form>
  <div v-if="formStatus === 'error'" class="error-message">Error processing URL: {{ errorMessage }}</div>
  <div v-else-if="formStatus === 'submitting'" class="loading-message">Parsing and converting recipe...</div>
  <div v-else-if="formStatus === 'success'" class="success-message">Success!</div>
  <div v-if="apiResponse">
    <BarkdownEditor :message="apiResponse.message" />
  </div>
  <!-- <div v-if="apiResponse">
    <p>{{ apiResponse.message }}</p>
  </div> -->
</template>

<script>
import BarkdownEditor from './components/BarkdownEditor.vue';

export default {
  data() {
    return {
      formData: {
        url: ""
      },
      apiResponse: null,
      errorMessage: null,
      formStatus: 'idle' // could be 'idle', 'submitting', 'success', 'error'
    };
  },
  methods: {
    async submitForm() {
      this.formStatus = 'submitting'
      try {
        const response = await fetch("http://0.0.0.0:5000", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(this.formData)
        });
        if (!response.ok) {
          this.formStatus = 'error'
          throw new Error(response.statusText);
        }
        this.formStatus = 'success'
        this.apiResponse = await response.json()
      } catch (error) {
        this.errorMessage = error.message;
      }
    }
  },
  components: {
    BarkdownEditor
  }
}
</script>

<!-- <style scoped>
form {
  background-color: #eeeeee;
  box-shadow: 0px 0px 4px;
  padding: 10px;
  max-width: 320px;
  margin: auto;
  margin-top: 30px;
  font-family: 'Monaco', courier, monospace
}
</style> -->

<style scoped>
form {
  padding: 10px 10px;
  background-color: #eeeeee;
  height: 2em;
  max-width: 20vw;
  margin: 20px auto 6px auto;
  border: solid 1px #efefef;
  display: flex;
}

form input {
  width: 70%;
}

form button {
  width: 30%;
}

.error-message {
  color: red;
  border: 1px solid red;
  padding: 10px 10px;
  background-color: #eeeeee;
  max-width: 20vw;
  margin: 0 auto;
}


.loading-message,
.success-message {
  color: black;
  border: 1px solid black;
  padding: 10px 10px;
  background-color: #eeeeee;
  max-width: 20vw;
  margin: 0 auto;
}
</style>