<template>
    <div class="contact-detail" :class="{ 'slide-in': show }">
      <!-- 顶部导航 -->
      <div class="header">
        <div class="back-button" @click="$emit('back')">
          <i class="icon-back"></i>
        </div>
        <div class="title">详细资料</div>
        <div class="more">
          <i class="icon-more"></i>
        </div>
      </div>
  
      <!-- 基本信息 -->
      <div class="detail-content">
        <div class="basic-info">
          <div class="avatar">
            <img :src="contact.avatar" alt="头像">
          </div>
          <div class="info">
            <div class="name">{{ contact.name }}</div>
            <div class="wxid">微信号：{{ contact.wxid || 'wxid_' + contact.id }}</div>
            <div class="region" v-if="contact.region">地区：{{ contact.region }}</div>
          </div>
        </div>
  
        <!-- 操作按钮 -->
        <div class="action-buttons">
          <div class="action-button">
            <i class="icon-message"></i>
            <span>发消息</span>
          </div>
          <div class="action-button">
            <i class="icon-video-call"></i>
            <span>视频通话</span>
          </div>
        </div>
  
        <!-- 社交信息 -->
        <div class="social-info">
          <div class="info-item">
            <span class="label">朋友圈</span>
            <i class="icon-arrow"></i>
          </div>
          <div class="info-item">
            <span class="label">更多信息</span>
            <i class="icon-arrow"></i>
          </div>
        </div>
  
        <!-- 标签设置 -->
        <div class="tags-section">
          <div class="section-header">
            <span>标签</span>
            <i class="icon-edit"></i>
          </div>
          <div class="tags-content">
            <div 
              v-for="tag in contact.tags" 
              :key="tag"
              class="tag"
            >
              {{ tag }}
            </div>
            <div class="tag add-tag" @click="showTagEditor = true">
              <i class="icon-plus"></i>
            </div>
          </div>
        </div>
  
        <!-- 备注和权限设置 -->
        <div class="settings-section">
          <div class="setting-item">
            <span class="label">备注名</span>
            <div class="value">
              <span>{{ contact.remarkName || '未设置' }}</span>
              <i class="icon-arrow"></i>
            </div>
          </div>
          <div class="setting-item">
            <span class="label">朋友权限</span>
            <div class="value">
              <span>{{ contact.privacy || '已开启' }}</span>
              <i class="icon-arrow"></i>
            </div>
          </div>
          <div class="setting-item">
            <span class="label">消息免打扰</span>
            <switch-button v-model="contact.muted" />
          </div>
          <div class="setting-item">
            <span class="label">置顶聊天</span>
            <switch-button v-model="contact.pinned" />
          </div>
        </div>
  
        <!-- 底部按钮 -->
        <div class="bottom-buttons">
          <button class="delete-button" @click="showDeleteConfirm = true">
            删除联系人
          </button>
          <button class="block-button" @click="showBlockConfirm = true">
            加入黑名单
          </button>
        </div>
      </div>
  
      <!-- 标签编辑弹窗 -->
      <div class="tag-editor" v-if="showTagEditor">
        <!-- 标签编辑器内容 -->
      </div>
  
      <!-- 确认弹窗 -->
      <confirm-dialog
        v-if="showDeleteConfirm"
        title="删除联系人"
        content="删除后将同时删除与该联系人的聊天记录"
        @confirm="handleDelete"
        @cancel="showDeleteConfirm = false"
      />
  
      <confirm-dialog
        v-if="showBlockConfirm"
        title="加入黑名单"
        content="加入黑名单后，您将不再收到对方的消息"
        @confirm="handleBlock"
        @cancel="showBlockConfirm = false"
      />
    </div>
  </template>
  
  <script>
  import { defineComponent, ref } from 'vue'
  import { useMainStore } from '@/store'
  import SwitchButton from '@/components/common/SwitchButton.vue'
  import ConfirmDialog from '@/components/common/ConfirmDialog.vue'
  
  export default defineComponent({
    name: 'ContactDetail',
  
    components: {
      SwitchButton,
      ConfirmDialog
    },
  
    props: {
      contact: {
        type: Object,
        required: true
      },
      show: {
        type: Boolean,
        default: false
      }
    },
  
    emits: ['back', 'delete', 'block'],
  
    setup(props, { emit }) {
      const store = useMainStore()
      const showTagEditor = ref(false)
      const showDeleteConfirm = ref(false)
      const showBlockConfirm = ref(false)
  
      const handleDelete = () => {
        emit('delete', props.contact)
        showDeleteConfirm.value = false
      }
  
      const handleBlock = () => {
        emit('block', props.contact)
        showBlockConfirm.value = false
      }
  
      return {
        showTagEditor,
        showDeleteConfirm,
        showBlockConfirm,
        handleDelete,
        handleBlock
      }
    }
  })
  </script>
  
  <style lang="scss">
  @import './detail.scss';
  </style>