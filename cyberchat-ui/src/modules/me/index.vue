<template>
  <div class="me-page">
    <!-- 用户信息部分 -->
    <div class="user-info">
      <div class="avatar">
        <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=User" alt="头像">
      </div>
      <div class="info">
        <div class="name">用户名</div>
        <div class="wxid">微信号：wxid_xxx</div>
      </div>
      <div class="qr-code">
        <i class="icon-qr"></i>
      </div>
      <i class="icon-arrow"></i>
    </div>

    <!-- 支付部分 -->
    <div class="me-section">
      <div class="me-item">
        <i class="icon-pay"></i>
        <span>支付</span>
        <i class="icon-arrow"></i>
      </div>
    </div>

    <!-- 收藏、相册等 -->
    <div class="me-section">
      <div class="me-item">
        <i class="icon-favorites"></i>
        <span>收藏</span>
        <i class="icon-arrow"></i>
      </div>
      <div class="me-item">
        <i class="icon-albums"></i>
        <span>相册</span>
        <i class="icon-arrow"></i>
      </div>
      <div class="me-item">
        <i class="icon-cards"></i>
        <span>卡包</span>
        <i class="icon-arrow"></i>
      </div>
      <div class="me-item">
        <i class="icon-sticker"></i>
        <span>表情</span>
        <i class="icon-arrow"></i>
      </div>
    </div>

    <!-- 设置部分 -->
    <div class="me-section">
      <div class="me-item">
        <i class="icon-settings"></i>
        <span>设置</span>
        <i class="icon-arrow"></i>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'Me'
})
</script>

<style lang="scss">
.me-page {
  height: 100%;
  background: #f7f7f7;
  overflow-y: auto;
  padding-bottom: calc(60px + env(safe-area-inset-bottom));
}

.user-info {
  display: flex;
  align-items: center;
  padding: 20px 16px;
  background: #fff;
  margin-bottom: 8px;

  .avatar {
    width: 64px;
    height: 64px;
    margin-right: 16px;
    
    img {
      width: 100%;
      height: 100%;
      border-radius: 6px;
    }
  }

  .info {
    flex: 1;
    min-width: 0;

    .name {
      font-size: 20px;
      font-weight: 500;
      margin-bottom: 4px;
      color: #000;
    }

    .wxid {
      font-size: 14px;
      color: #999;
    }
  }

  .qr-code {
    width: 24px;
    height: 24px;
    margin-right: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .icon-arrow {
    width: 8px;
    height: 8px;
    border-top: 2px solid #c7c7cc;
    border-right: 2px solid #c7c7cc;
    transform: rotate(45deg);
  }
}

.me-section {
  background: #fff;
  margin-bottom: 8px;
}

.me-item {
  display: flex;
  align-items: center;
  padding: 12px 16px;
  border-bottom: 1px solid #f5f5f5;

  &:last-child {
    border-bottom: none;
  }

  i:first-child {
    width: 24px;
    height: 24px;
    margin-right: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  span {
    flex: 1;
    font-size: 17px;
    color: #000;
  }

  .icon-arrow {
    width: 8px;
    height: 8px;
    border-top: 2px solid #c7c7cc;
    border-right: 2px solid #c7c7cc;
    transform: rotate(45deg);
  }
}

// 图标样式
.icon-pay::before {
  content: '';
  display: inline-block;
  width: 24px;
  height: 24px;
  background: url('https://api.iconify.design/material-symbols:payments.svg?color=%2307C160') no-repeat center;
  background-size: contain;
}

.icon-favorites::before {
  content: '';
  display: inline-block;
  width: 24px;
  height: 24px;
  background: url('https://api.iconify.design/material-symbols:star.svg?color=%2307C160') no-repeat center;
  background-size: contain;
}

.icon-albums::before {
  content: '';
  display: inline-block;
  width: 24px;
  height: 24px;
  background: url('https://api.iconify.design/material-symbols:photo-library.svg?color=%2307C160') no-repeat center;
  background-size: contain;
}

.icon-cards::before {
  content: '';
  display: inline-block;
  width: 24px;
  height: 24px;
  background: url('https://api.iconify.design/material-symbols:credit-card.svg?color=%2307C160') no-repeat center;
  background-size: contain;
}

.icon-sticker::before {
  content: '';
  display: inline-block;
  width: 24px;
  height: 24px;
  background: url('https://api.iconify.design/material-symbols:emoji-emotions.svg?color=%2307C160') no-repeat center;
  background-size: contain;
}

.icon-settings::before {
  content: '';
  display: inline-block;
  width: 24px;
  height: 24px;
  background: url('https://api.iconify.design/material-symbols:settings.svg?color=%2307C160') no-repeat center;
  background-size: contain;
}
</style> 