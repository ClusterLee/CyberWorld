<template>
  <div class="dialog-overlay" @click="handleOverlayClick">
    <div class="dialog-container" @click.stop>
      <div class="dialog-content">
        <div class="dialog-title" v-if="title">{{ title }}</div>
        <div class="dialog-message">{{ content }}</div>
      </div>
      <div class="dialog-buttons">
        <button 
          class="cancel-button"
          @click="$emit('cancel')"
        >
          {{ cancelText }}
        </button>
        <button 
          class="confirm-button"
          :class="{ 'danger': type === 'danger' }"
          @click="$emit('confirm')"
        >
          {{ confirmText }}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'ConfirmDialog',

  props: {
    title: {
      type: String,
      default: ''
    },
    content: {
      type: String,
      required: true
    },
    type: {
      type: String,
      default: 'default',
      validator: (value) => ['default', 'danger'].includes(value)
    },
    confirmText: {
      type: String,
      default: '确定'
    },
    cancelText: {
      type: String,
      default: '取消'
    },
    closeOnClickOverlay: {
      type: Boolean,
      default: true
    }
  },

  emits: ['confirm', 'cancel'],

  setup(props, { emit }) {
    const handleOverlayClick = () => {
      if (props.closeOnClickOverlay) {
        emit('cancel')
      }
    }

    return {
      handleOverlayClick
    }
  }
})
</script>

<style scoped>
.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2000;
  animation: fadeIn 0.2s ease;
}

.dialog-container {
  width: 280px;
  background: #fff;
  border-radius: 12px;
  overflow: hidden;
  animation: scaleIn 0.2s ease;
}

.dialog-content {
  padding: 20px;
  text-align: center;
}

.dialog-title {
  font-size: 17px;
  font-weight: 500;
  margin-bottom: 8px;
}

.dialog-message {
  font-size: 15px;
  color: #666;
  line-height: 1.4;
}

.dialog-buttons {
  display: flex;
  border-top: 1px solid #eee;
}

.dialog-buttons button {
  flex: 1;
  height: 44px;
  border: none;
  background: #fff;
  font-size: 17px;
  cursor: pointer;

  &:active {
    background: #f5f5f5;
  }

  &.cancel-button {
    border-right: 1px solid #eee;
    color: #666;
  }

  &.confirm-button {
    color: #07c160;

    &.danger {
      color: #f43530;
    }
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes scaleIn {
  from {
    transform: scale(0.8);
    opacity: 0;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}
</style> 