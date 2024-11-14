import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useMainStore = defineStore('main', () => {
  // 状态
  const currentTab = ref('wechat')
  const showChat = ref(false)
  const currentChat = ref(null)
  const searchText = ref('')
  const searchResults = ref([])
  
  // 聊天列表数据
  const chats = ref([
    {
      id: '1',
      name: '张三',
      avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Felix',
      lastMessage: '你好啊',
      time: '12:30',
      unread: 2,
      messages: []
    },
    {
      id: '2',
      name: '李四',
      avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Bella',
      lastMessage: '在吗？',
      time: '11:45',
      unread: 0,
      messages: []
    }
  ])

  // 通讯录数据
  const contactSections = ref([
    {
      letter: 'A',
      contacts: [
        {
          id: 'a1',
          name: '阿里',
          avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Ali'
        }
      ]
    },
    {
      letter: 'B',
      contacts: [
        {
          id: 'b1',
          name: '白云',
          avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Bai'
        }
      ]
    }
  ])

  // 计算属性
  const hasUnreadMessages = computed(() => {
    return chats.value.some(chat => chat.unread > 0)
  })

  // 方法
  const openChatDetail = (chat) => {
    currentChat.value = chat
    showChat.value = true
    // 清除未读消息
    if (chat.unread) {
      chat.unread = 0
    }
  }

  const closeChatDetail = () => {
    showChat.value = false
    currentChat.value = null
  }

  const sendMessage = (chatId, message) => {
    const chat = chats.value.find(c => c.id === chatId)
    if (chat) {
      chat.messages.push(message)
      chat.lastMessage = message.content
      chat.time = new Date().toLocaleTimeString()
    }
  }

  const handleSearch = () => {
    if (!searchText.value) {
      searchResults.value = []
      return
    }
    
    searchResults.value = contactSections.value.reduce((results, section) => {
      return results.concat(
        section.contacts.filter(contact => 
          contact.name.toLowerCase().includes(searchText.value.toLowerCase())
        )
      )
    }, [])
  }

  const openContactDetail = (contact) => {
    // 实现联系人详情页面打开逻辑
  }

  const handleLetterTouchStart = (event, letter) => {
    event.preventDefault()
    scrollToLetter(letter)
  }

  const scrollToLetter = (letter) => {
    const element = document.querySelector(`[data-letter="${letter}"]`)
    if (element) {
      const container = document.querySelector('.contact-list')
      const containerRect = container.getBoundingClientRect()
      const elementRect = element.getBoundingClientRect()
      const offset = elementRect.top - containerRect.top
      
      container.scrollTo({
        top: container.scrollTop + offset - 60,
        behavior: 'smooth'
      })
    }
  }

  return {
    currentTab,
    showChat,
    currentChat,
    chats,
    contactSections,
    searchText,
    searchResults,
    hasUnreadMessages,
    openChatDetail,
    closeChatDetail,
    sendMessage,
    handleSearch,
    openContactDetail,
    handleLetterTouchStart,
    scrollToLetter
  }
}) 