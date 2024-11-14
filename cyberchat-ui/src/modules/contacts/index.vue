<template>
  <div class="contacts-page">
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

    <!-- 搜索结果 -->
    <div class="search-results" v-if="searchText && searchResults.length">
      <div 
        class="contact-item" 
        v-for="contact in searchResults" 
        :key="contact.id"
        @click="openContactDetail(contact)"
      >
        <div class="avatar">
          <img :src="contact.avatar" alt="头像">
        </div>
        <div class="name">{{ contact.name }}</div>
      </div>
    </div>

    <!-- 联系人列表 -->
    <div class="contact-list" v-show="!searchText">
      <!-- 特殊联系人 -->
      <div class="special-section">
        <div class="contact-item">
          <div class="avatar special-avatar green-bg">
            <img src="https://api.iconify.design/material-symbols:group.svg?color=white&width=18" alt="新的朋友" class="icon-new-friend">
          </div>
          <div class="name">新的朋友</div>
        </div>
        <div class="contact-item">
          <div class="avatar special-avatar green-bg">
            <img src="https://api.iconify.design/material-symbols:group.svg?color=white&width=18" alt="群聊" class="icon-group">
          </div>
          <div class="name">群聊</div>
        </div>
        <div class="contact-item">
          <div class="avatar special-avatar green-bg">
            <img src="https://api.iconify.design/material-symbols:sell.svg?color=white&width=14" alt="标签" class="icon-tag">
          </div>
          <div class="name">标签</div>
        </div>
        <div class="contact-item">
          <div class="avatar special-avatar green-bg">
            <img src="https://api.iconify.design/material-symbols:public.svg?color=white&width=18" alt="公众号" class="icon-official">
          </div>
          <div class="name">公众号</div>
        </div>
      </div>

      <!-- 联系人分组 -->
      <div 
        v-for="section in contactSections" 
        :key="section.letter" 
        class="contact-section"
      >
        <div class="section-title" :data-letter="section.letter">
          {{ section.letter }}
        </div>
        <div 
          class="contact-item"
          v-for="contact in section.contacts"
          :key="contact.id"
          @click="openContactDetail(contact)"
        >
          <div class="avatar">
            <img :src="contact.avatar" alt="头像">
          </div>
          <div class="name">{{ contact.name }}</div>
        </div>
      </div>
    </div>

    <!-- 字母导航 -->
    <div 
      class="letter-index"
      @touchstart="handleLetterTouchStart"
      @touchmove="handleLetterTouchMove"
      @touchend="handleLetterTouchEnd"
    >
      <div 
        v-for="letter in letters" 
        :key="letter"
        class="letter-item"
        :class="{ 'active': currentLetter === letter }"
      >
        {{ letter }}
      </div>
    </div>

    <!-- 当前选中字母提示 -->
    <div 
      class="letter-indicator"
      v-show="showLetterIndicator"
    >
      {{ currentLetter }}
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, computed } from 'vue'
import { useMainStore } from '@/store'

export default defineComponent({
  name: 'Contacts',

  setup() {
    const store = useMainStore()
    const searchText = ref('')
    const currentLetter = ref('')
    const showLetterIndicator = ref(false)
    let indicatorTimer = null

    const letters = ['↑', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '#']

    const searchResults = computed(() => {
      if (!searchText.value) return []
      return store.contactSections.reduce((results, section) => {
        return results.concat(
          section.contacts.filter(contact => 
            contact.name.toLowerCase().includes(
              searchText.value.toLowerCase()
            )
          )
        )
      }, [])
    })

    return {
      searchText,
      searchResults,
      contactSections: store.contactSections,
      letters,
      handleSearch: store.handleSearch,
      openContactDetail: store.openContactDetail,
      handleLetterTouchStart: store.handleLetterTouchStart,
      handleLetterTouchMove: store.handleLetterTouchMove,
      handleLetterTouchEnd: store.handleLetterTouchEnd,
      currentLetter,
      showLetterIndicator
    }
  }
})
</script>

<style lang="scss">
@import './style.scss';
</style> 