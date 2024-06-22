<template>
  <div class="breadDoctor">
    <ul>
      <li>
        <router-link to="/back_choose_date" class="breadDoctor_link"
          >預約日</router-link
        >
      </li>
      <li>
        <router-link to="/historical_amount" class="breadDoctor_link"
          >歷史金額</router-link
        >
      </li>
      <li>
        <router-link to="/report" class="breadDoctor_link">報表</router-link>
      </li>
      <li>
        <router-link to="/setting" class="breadDoctor_link">設定</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    items: {
      type: Array,
    },
  },
};
</script>

<style scoped lang="scss">
@import "@/assets/_variables.scss";

.breadDoctor {
  font-size: 16px;
  color: $primaryDark;
  margin-bottom: 20px;
  font-weight: 700;

  ul {
    display: flex;
    gap: 40px;
    cursor: pointer;
    list-style-type: none;

    li {
      &:hover {
        opacity: 0.7;
      }

      .breadDoctor_link {
        color: $primaryDark;
        text-decoration: none;
      }
    }
  }
}
</style>
