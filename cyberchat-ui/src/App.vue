<template>
  <div class="wechat-container">
    <!-- 主页面 -->
    <div class="page main-page" :class="{ 'slide-out': showChat }">
      <!-- 顶部状态栏 -->
      <div class="header">
        <div class="title">{{ getCurrentTabName }}</div>
      </div>

      <!-- 主要内容区域 -->
      <router-view></router-view>

      <!-- 底部导航栏 -->
      <div class="tab-bar">
        <div 
          v-for="tab in tabs" 
          :key="tab.id"
          class="tab-item"
          :class="{ 'active': currentTab === tab.id }"
          @click="switchTab(tab.id)"
        >
          <div class="tab-icon">
            <i :class="'icon-' + tab.id"></i>
            <div v-if="tab.unread" class="badge">
              {{ tab.unread > 99 ? '99+' : tab.unread }}
            </div>
            <div v-if="tab.hasNew" class="red-dot"></div>
          </div>
          <span>{{ tab.name }}</span>
        </div>
      </div>
    </div>

    <!-- 聊天详情页 -->
    <ChatDetail 
      v-if="showChat" 
      :chat="currentChat"
      @back="closeChat"
    />
  </div>
</template>

<script>
import { defineComponent, ref, computed } from 'vue'
import { useMainStore } from './store'
import ChatDetail from './components/chat/ChatDetail.vue'

export default defineComponent({
  name: 'App',

  components: {
    ChatDetail
  },

  setup() {
    const store = useMainStore()
    const currentTab = ref('wechat')
    const showChat = ref(false)
    const currentChat = ref(null)

    const tabs = [
      { id: 'wechat', name: '微信', unread: 0 },
      { id: 'contacts', name: '通讯录', hasNew: false },
      { id: 'discover', name: '发现', hasNew: false },
      { id: 'me', name: '我', hasNew: false }
    ]

    const getCurrentTabName = computed(() => {
      const tab = tabs.find(t => t.id === currentTab.value)
      return tab ? tab.name : '微信'
    })

    const switchTab = (tabId) => {
      currentTab.value = tabId
    }

    return {
      tabs,
      currentTab,
      showChat,
      currentChat,
      getCurrentTabName,
      switchTab
    }
  }
})
</script>

<style scoped>
/* 状态栏 样式 */
.header {
    height: 44px;
    min-height: 44px;
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 15px;
    position: sticky;
    top: 0;
    z-index: 100;
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
    box-sizing: border-box;
}

.title {
    font-size: 17px;
    font-weight: 500;
    color: #000;
    text-align: center;
    flex: 1;
    margin: 0 48px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* TabBar 样式 */
.tab-bar {
  height: 60px;
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  display: flex;
  justify-content: space-around;
  align-items: center;
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  padding-bottom: env(safe-area-inset-bottom);
  border-top: 1px solid rgba(0, 0, 0, 0.1);
  z-index: 99;
}

.tab-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 8px 0;
  cursor: pointer;

  .tab-icon {
    position: relative;
    width: 24px;
    height: 24px;
    margin-bottom: 4px;
  }

  i {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  span {
    font-size: 12px;
    color: #999;
  }

  &.active span {
    color: #07c160;
  }

  .badge {
    position: absolute;
    top: -8px;
    right: -8px;
    min-width: 16px;
    height: 16px;
    line-height: 16px;
    text-align: center;
    background: #f43530;
    color: #fff;
    border-radius: 8px;
    font-size: 12px;
    padding: 0 4px;
    
    &.large {
      font-size: 10px;
      padding: 0 2px;
    }
  }

  .red-dot {
    position: absolute;
    top: -4px;
    right: -4px;
    width: 8px;
    height: 8px;
    background: #f43530;
    border-radius: 50%;
  }
}

/* 图标样式 */
.icon-wechat::before {
  content: '';
  display: inline-block;
  width: 100%;
  height: 100%;
  background: url('https://cdn-icons-png.flaticon.com/512/1250/1250592.png') no-repeat center;
  background-size: contain;
  opacity: 0.7;
}

.icon-contacts::before {
  content: '';
  display: inline-block;
  width: 100%;
  height: 100%;
  background: url('https://cdn-icons-png.flaticon.com/512/1250/1250592.png') no-repeat center;
  background-size: contain;
  opacity: 0.7;
}

.icon-discover::before {
  content: '';
  display: inline-block;
  width: 100%;
  height: 100%;
  background: url('https://cdn-icons-png.flaticon.com/512/2089/2089363.png') no-repeat center;
  background-size: contain;
  opacity: 0.7;
}

.icon-me::before {
  content: '';
  display: inline-block;
  width: 100%;
  height: 100%;
  background: url('https://cdn-icons-png.flaticon.com/512/1077/1077063.png') no-repeat center;
  background-size: contain;
  opacity: 0.7;
}

/* 激活状态的图标样式 */
.tab-item.active i::before {
  opacity: 1;
  filter: invert(57%) sepia(75%) saturate(1304%) hue-rotate(93deg) brightness(95%) contrast(89%);
}
</style>
