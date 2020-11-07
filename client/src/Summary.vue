<template>
  <div class="m-b-3 rounded border-gray-600 flex flex-row">
    <div class="p-3 bg-gray-200">
    <h1 class="text-2xl">{{ summary.title }}</h1>
    <span>{{summary.date}}</span>
    <ul class="ml-4">
      <li class="mb-2">{{ summary.first }}</li>
      <li>{{ summary.second }}</li>
    </ul>
    </div>
    <div class="p-3">
      <button class="p-2 border border-gray-400 rounded hover:bg-white hover:border-gray-500">
      <a title="Open Article in New Tab" target="_blank" :href="summary.link"><external-link-icon /></a>
      </button>
    </div>
  </div>
</template>

<script>
import { ExternalLinkIcon } from 'vue-feather-icons'

export default {
  name: 'Summary',
  components: { ExternalLinkIcon },
  props: {
    summary: {
      type: Object,
      required: true,
    }
  }
}
</script>

<style scoped>
ul {list-style-type: square;}
</style>