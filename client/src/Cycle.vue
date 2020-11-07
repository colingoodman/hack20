<template>
  <div>
    <h2 class="flex mx-auto text-2xl w-100 justify-center text-center mb-3 border-b-2 border-gray-600"><clock-icon class="py-auto my-auto mr-2" />{{ cycle.date }}</h2>
    <div>
      <Summary class="mb-3" v-for="summary in cycle.summaries" :summary="summary" :key="summary.title" />
    </div>
  </div>
</template>

<script>
import Summary from './Summary'
import { ClockIcon } from 'vue-feather-icons'

export default {
  name: 'Cycle',
  components: { Summary, ClockIcon },
  props: {
    cycle: {
      type: Object,
      required: true,
    }
  }
}
</script>