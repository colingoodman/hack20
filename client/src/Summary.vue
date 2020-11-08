<template>
  <div class="m-b-3 rounded border-gray-600 flex flex-row">
    <div class="p-3 bg-gray-200">
    <h1 class="text-2xl">{{ summary.title }}</h1>
    <span>{{summary.date}}</span>
    <ul class="ml-8">
      <li class="mb-2">{{ summary.first }}</li>
      <li>{{ summary.second }}</li>
    </ul>
    <span v-if="summary.source" class="text-gray-700">from {{ summary.source }}</span>
    </div>
    <div>
      <button class="p-2 text-gray-600 rounded hover:bg-white hover:text-gray-800">
      <a title="Open Article in New Tab" target="_blank" :href="summary.url"><external-link-icon /></a>
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
  },
}
</script>

<style scoped>
ul {list-style-type: square;}
</style>