<template>
  <div class="loading-spinner" :class="{ 'fullscreen': fullscreen }">
    <div class="spinner-container">
      <div class="spinner"></div>
      <div v-if="text" class="loading-text">{{ text }}</div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'LoadingSpinner',

  props: {
    text: {
      type: String,
      default: '加载中...'
    },
    fullscreen: {
      type: Boolean,
      default: false
    }
  }
})
</script>

<style scoped>
.loading-spinner {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 16px;
}

.loading-spinner.fullscreen {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(255, 255, 255, 0.9);
  z-index: 2000;
}

.spinner-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.spinner {
  width: 24px;
  height: 24px;
  border: 2px solid #07c160;
  border-top-color: transparent;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

.loading-text {
  margin-top: 16px;
  font-size: 16px;
  color: #333;
}
</style> 