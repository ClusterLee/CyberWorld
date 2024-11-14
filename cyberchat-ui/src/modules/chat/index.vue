<template>
  <div class="chat-list-page">
    <!-- 搜索框 -->
    <div class="search-container">
      <div class="search-box">
        <i class="icon-search"></i>
        <input 
          type="text" 
          v-model="searchText"
          placeholder="搜索"
          @input="handleSearch"
        >
      </div>
    </div>

    <!-- 聊天列表 -->
    <div class="chat-list">
      <div 
        v-for="chat in chats" 
        :key="chat.id"
        class="chat-item"
        @click="openChat(chat)"
      >
        <div class="avatar">
          <img :src="chat.avatar" alt="头像">
          <div 
            v-if="chat.unread" 
            class="badge"
            :class="{ 'large': chat.unread > 99 }"
          >
            {{ chat.unread > 99 ? '99+' : chat.unread }}
          </div>
        </div>
        <div class="content">
          <div class="top">
            <div class="name">{{ chat.name }}</div>
            <div class="time">{{ chat.time }}</div>
          </div>
          <div class="bottom">
            <div class="message">{{ chat.lastMessage }}</div>
            <div v-if="chat.muted" class="mute-icon">
              <i class="icon-mute"></i>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, computed } from 'vue'
import { useMainStore } from '@/store'

export default defineComponent({
  name: 'ChatList',

  setup() {
    const store = useMainStore()
    const searchText = ref('')

    const chats = computed(() => {
      if (!searchText.value) {
        return store.chats
      }
      return store.chats.filter(chat => 
        chat.name.toLowerCase().includes(searchText.value.toLowerCase()) ||
        chat.lastMessage.toLowerCase().includes(searchText.value.toLowerCase())
      )
    })

    const openChat = (chat) => {
      store.openChatDetail(chat)
    }

    const handleSearch = () => {
      // 实时搜索逻辑
    }

    return {
      searchText,
      chats,
      openChat,
      handleSearch
    }
  }
})
</script>

<style scoped>
@import './style.css';
</style> 