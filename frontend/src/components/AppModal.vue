<template>
  <div class="app-modal-component"
    :class="{ open }"
  >
    <div class="app-modal-backdrop" @click="dismiss" />
    <div class="app-modal">
      <div class="close" @click="dismiss" v-if="showCloseButon" />
      <slot />
    </div>
  </div>
</template>

<script lang="ts">
import { createComponent, PropType, computed } from '@vue/composition-api'

export default createComponent({
  name: 'AppModal',
  props: {
    open: {
      type: Boolean,
      default: false
    },
    dismiss: {
      type: Function
    },
    showCloseButon: {
      type: Boolean,
      default: true
    }
  }
})
</script>

<style lang="scss" scoped>
@import '../styles/variables';

.app-modal-component {
  z-index: 1;
  position: fixed;

  justify-content: center;
  align-items: center;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;

  padding: 45px 16px;

  display: none;

  &.open {
    display: flex;
  }
}

.app-modal-backdrop {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.4);
  z-index: 998;
}

.app-modal {
  z-index: 999;

  border-radius: 3px;
  border: solid 2px $primary-color;
  background-color: $background-color;

  padding: 27px 22px;

  position: absolute;
  top: 90px;
  max-height: calc(100vh - 110px);
  overflow: auto;

  .close {
    position: absolute;
    top: 24px;
    right: 22px;

    width: 24px;
    height: 24px;
    padding-top: 12px;
    cursor: pointer;

    &::before, &::after {
      display: block;
      content: '';
      width: 100%;
      height: 3px;
      background: #000;
      transform-origin: center;
      position: absolute;
      border-radius: 5px;
    }

    &::before {
      transform: rotate(45deg);
    }

    &::after {
      transform: rotate(-45deg);
    }
  }
}
</style>
