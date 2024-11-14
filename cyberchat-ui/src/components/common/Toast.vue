<template>
  <transition name="fade">
    <div v-if="visible" class="toast" :class="type">
      <i v-if="type !== 'default'" :class="iconClass"></i>
      <span>{{ message }}</span>
    </div>
  </transition>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue'

export default defineComponent({
  name: 'Toast',

  props: {
    message: {
      type: String,
      required: true
    },
    type: {
      type: String,
      default: 'default',
      validator: (value) => ['default', 'success', 'error', 'warning'].includes(value)
    },
    duration: {
      type: Number,
      default: 2000
    }
  },

  emits: ['close'],

  setup(props, { emit }) {
    const visible = ref(false)

    const iconClass = {
      success: 'icon-success',
      error: 'icon-error',
      warning: 'icon-warning'
    }[props.type]

    onMounted(() => {
      visible.value = true
      if (props.duration > 0) {
        setTimeout(() => {
          visible.value = false
          setTimeout(() => emit('close'), 300)
        }, props.duration)
      }
    })

    return {
      visible,
      iconClass
    }
  }
})
</script>

<style lang="scss" scoped>
.toast {
  position: fixed;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  padding: 12px 20px;
  background: rgba(0, 0, 0, 0.8);
  border-radius: 4px;
  color: #fff;
  font-size: 14px;
  display: flex;
  align-items: center;
  z-index: 3000;
  max-width: 80%;
  word-break: break-word;
  text-align: center;
  transition: opacity 0.3s ease;

  i {
    margin-right: 8px;
    font-size: 20px;
  }

  &.success i {
    color: #07c160;
  }

  &.error i {
    color: #f43530;
  }

  &.warning i {
    color: #ff9c0b;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style> 