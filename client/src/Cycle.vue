<template>
  <div>
    <h2 class="flex mx-auto text-2xl w-100 justify-between text-center border-b-2 border-gray-600">
      <span class="mr-2 flex"><clock-icon class="py-auto my-auto mr-2" />{{ formatDate(new Date()) }}</span>
      <span class="text-gray-400">&nbsp;{{ dateDistance(new Date()) }}</span>
      </h2>
    <div>
      <Summary class="mb-3" v-for="summary in cycle.summaries" :summary="summary" :key="summary.title" />
    </div>
  </div>
</template>

<script>
import Summary from './Summary'
import { ClockIcon } from 'vue-feather-icons'
import { formatDistance, format } from 'date-fns'

export default {
  name: 'Cycle',
  components: { Summary, ClockIcon },
  props: {
    cycle: {
      type: Object,
      required: true,
    }
  },
  methods: {
    dateDistance(date) {
      return formatDistance(new Date(date), new Date(), { addSuffix: true })
    },
    formatDate(date) {
      return format(new Date(date), 'PP  p')
    }
  }
}
</script>