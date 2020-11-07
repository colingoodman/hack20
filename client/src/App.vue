<template>
  <div
    id="app"
    class="bg-white justify-center max-h-screen overflow-y-auto"
  >
  <marquee direction="right">QUIK NEWS</marquee>
    <div class="text-gray-800 p-1 max-w-4xl mx-auto">
      <div class="p-2">
        <h1 class="text-4xl">Quik News</h1>
      </div>
      <Cycle class="mb-16" v-for="cycle in cycles" :cycle="cycle" :key="cycle.date" />
      <button @click="getSummaries">GET</button>
    </div>
  </div>
</template>

<script>
import cycles from '../../file.json'
import Cycle from './Cycle.vue'

export default {
  name: 'App',
  components: { Cycle },
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
</style>
