<template>
  <div
    id="app"
    class="bg-white justify-center max-h-screen overflow-y-auto"
  >
    <div class="text-gray-800 p-1 max-w-4xl mx-auto">
      <div class="text-4xl my-4">
        <img class="inline mr-3" width="64px" src="nutshell.png" />
        <h1 class="inline">In A Nutshell</h1>
      </div>
      <Cycle class="mb-8" v-for="cycle in cycles" :cycle="cycle" :key="cycle.date" />
      <div v-if="loading" class="loader mx-auto" />
      <button v-if="!getDisabled && !loading" class="text-4xl flex mx-auto hover:text-gray-600" @click="getSummaries"><refresh-cw-icon size="1x" class="my-auto py-auto mr-3" />Give me recent news!</button>
    </div>
  </div>
</template>

<script>
import cycles from '../../example.json'
import Cycle from './Cycle.vue'
import { RefreshCwIcon } from 'vue-feather-icons'

export default {
  name: 'App',
  components: { Cycle, RefreshCwIcon },
  data() {
    return {
      cycles: cycles,
      getDisabled: false,
      loading: false,
    }
  },
  methods: {
    getSummaries() {
      this.loading = true;
      const Http = new XMLHttpRequest();
      const url='https://summarizer-ytwjcsc2wq-uc.a.run.app/api/v1/news';
      Http.open("GET", url);
      Http.send();

      Http.onreadystatechange = (e) => {
        this.cycles = [JSON.parse(Http.responseText)]
        this.getDisabled = true
        this.loading = false
      }
    },
  }
}
</script>

<style>
@tailwind base;
@tailwind components;
@tailwind utilities;

body
{
    font-family: 'Helvetica', 'Arial', sans-serif;
}

.loader {
  border: 16px solid #f3f3f3;
  border-top: 16px solid #666;
  border-radius:50%;
  width:20px;
  height: 20px;
  animation: spin 2s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% {transform: rotate(360deg); }
}
</style>
