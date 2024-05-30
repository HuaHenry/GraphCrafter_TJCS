<template>
  <div id="tabs" class="container">
    <div class="tabs">
      <a v-for="item in tabs" :key="item.tab" @click="activetab = item.tab" :class="[activetab === item.tab ? 'active' : '']">
        <slot :name="'tab-'+item.tab">{{ item.tab }}</slot>
      </a>
    </div>

    <div class="content">
      <div v-for="item in tabs" :key="item.tab" v-show="activetab === item.tab" class="tabcontent">
        <slot :name="'tabContent-'+item.tab">{{ item.content }}</slot>
      </div>
    </div>
  </div>
</template>


<script>
  export default {
    data() {
      return {
        el: "#tabs",
        activetab: 1,
        tabs: [
          {tab: 1, content: 'Tab 1'},
          {tab: 2, content: 'Tab 2'},
          {tab: 3, content: 'Tab 3'},
        ]
      };
    },
  };
</script>
<style lang="scss" scoped>
  .tabs {
    overflow: hidden;
    margin-left: 20px;
    margin-bottom: -2px; 
  }

  .tabs ul {
    list-style-type: none;
    margin-left: 20px;
  }

  .tabs a {
    cursor: pointer;
    display: inline-flex;
    padding: 12px 24px;
    transition: background-color 0.2s;
    border: 1px solid #ccc;
    border-right: none;
    background-color: #f1f1f1;
    border-radius: 10px 10px 0 0;
    font-weight: bold;
  }
  .tabs a:last-child {
    border-right: 1px solid #ccc;
  }

  /* Change background color of tabs on hover */
  .tabs a:hover {
    background-color: #aaa;
    color: #fff;
  }

  /* Styling for active tab */
  .tabs a.active {
    background-color: #fff;
    color: #484848;
    border-bottom: 2px solid #fff;
    cursor: default;
  }

  /* Style the tab content */
  .tabcontent {
    padding: 30px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 3px 3px 6px #e1e1e1;
  }
</style>
