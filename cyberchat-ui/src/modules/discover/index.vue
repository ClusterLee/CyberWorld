<template>
  <div class="discover-page">
    <div class="discover-list">
      <!-- 朋友圈和视频号 -->
      <div class="discover-section">
        <div class="discover-item">
          <img src="https://api.iconify.design/material-symbols:camera.svg?color=%23FF9C0B" alt="朋友圈" class="discover-icon">
          <span>朋友圈</span>
          <i class="icon-arrow"></i>
        </div>
        <div class="discover-item">
          <img src="https://api.iconify.design/material-symbols:play-circle.svg?color=%23FA9D3B" alt="视频号" class="discover-icon">
          <span>视频号</span>
          <i class="icon-arrow"></i>
        </div>
      </div>

      <!-- AI创作能力入口 -->
      <div class="discover-section">
        <div class="discover-item">
          <img src="https://api.iconify.design/material-symbols:brush.svg?color=%23FF6B6B" alt="画一画" class="discover-icon">
          <span>画一画</span>
          <i class="icon-arrow"></i>
        </div>
        <div class="discover-item">
          <img src="https://api.iconify.design/material-symbols:edit-note.svg?color=%234A90E2" alt="写一写" class="discover-icon">
          <span>写一写</span>
          <i class="icon-arrow"></i>
        </div>
        <div class="discover-item">
          <img src="https://api.iconify.design/material-symbols:music-note.svg?color=%23FFB900" alt="唱一唱" class="discover-icon">
          <span>唱一唱</span>
          <i class="icon-arrow"></i>
        </div>
        <div class="discover-item">
          <img src="https://api.iconify.design/material-symbols:fiber-smart-record.svg?color=%23B066FF" alt="录一录" class="discover-icon">
          <span>录一录</span>
          <i class="icon-arrow"></i>
        </div>
      </div>

      <!-- 扫一扫和摇一摇部分 -->
      <div class="discover-section">
        <div class="discover-item">
          <img src="https://api.iconify.design/material-symbols:qr-code-scanner.svg?color=%2307C160" alt="扫一扫" class="discover-icon">
          <span>扫一扫</span>
          <i class="icon-arrow"></i>
        </div>
        <div class="discover-item">
          <img src="https://api.iconify.design/material-symbols:vibration.svg?color=%2307C160" alt="摇一摇" class="discover-icon">
          <span>摇一摇</span>
          <i class="icon-arrow"></i>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'Discover'
})
</script>

<style lang="scss">
.discover-page {
  background: #f7f7f7;
  height: 100%;
  overflow-y: auto;
}

.discover-list {
  padding-top: 10px;
}

.discover-section {
  margin-bottom: 8px;
  background: #fff;
}

.discover-item {
  display: flex;
  align-items: center;
  padding: 12px 16px;
  background: #fff;
  border-bottom: 1px solid #f5f5f5;

  &:last-child {
    border-bottom: none;
  }

  .discover-icon {
    width: 24px;
    height: 24px;
    margin-right: 12px;
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
</style> 