<template>
  <div 
    class="switch-button"
    :class="{ 'active': modelValue, 'disabled': disabled }"
    @click="toggle"
  >
    <div class="switch-handle"></div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'SwitchButton',

  props: {
    modelValue: {
      type: Boolean,
      default: false
    },
    disabled: {
      type: Boolean,
      default: false
    }
  },

  emits: ['update:modelValue', 'change'],

  setup(props, { emit }) {
    const toggle = () => {
      if (props.disabled) return
      
      const newValue = !props.modelValue
      emit('update:modelValue', newValue)
      emit('change', newValue)
    }

    return {
      toggle
    }
  }
})
</script>

<style scoped>
.switch-button {
  width: 51px;
  height: 31px;
  background: #e5e5e5;
  border-radius: 31px;
  position: relative;
  cursor: pointer;
  transition: background-color 0.3s ease;
  flex-shrink: 0;
}

.switch-button.active {
  background: #07c160;
}

.switch-button.active .switch-handle {
  transform: translateX(22px);
}

.switch-button.disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.switch-handle {
  width: 27px;
  height: 27px;
  background: #fff;
  border-radius: 50%;
  position: absolute;
  top: 2px;
  left: 2px;
  transition: transform 0.3s ease;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}
</style> 