<template>
  <div
    id="app"
    class="bg-white justify-center max-h-screen overflow-y-auto"
  >
    <div class="text-gray-800 p-1 max-w-4xl mx-auto">
      <div class="text-4xl flex justify-between">
        <h1 class="inline">Quik News</h1>
        <button class="text-gray-600 rounded hover:bg-white hover:text-gray-800"><refresh-cw-icon /></button>
      </div>
      <Cycle class="mb-16" v-for="cycle in cycles" :cycle="cycle" :key="cycle.date" />
      <button @click="getSummaries">GET</button>
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
      cycles: cycles
    }
  },
  methods: {
    getSummaries() {
      const Http = new XMLHttpRequest();
      const url='https://hackkstate2020.uc.r.appspot.com/api/v1/resources/books/all';
      Http.open("GET", url);
      Http.send();

      Http.onreadystatechange = (e) => {
        console.log(Http.responseText)
      }
    },
    getSummaries2() {
      const url='https://hackkstate2020.uc.r.appspot.com/api/v1/resources/books/all';
      fetch(url,{header:{'Access-Control-Allow-Origin':'*'}})
    }
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
</style>
