<script>
import TheCircleProgress from "../components/TheCircleProgress.vue";
import BreadCrumbs from "../components/BreadCrumbs.vue";
import Calendar from "../components/Calendar.vue";
import { onMounted, reactive, ref } from "vue";
import { getListAPI,postRegisterAPI } from "@/api/api";
export default {
  components: {
    TheCircleProgress,
    BreadCrumbs,
    Calendar,
  },
  setup() {
    const breadcrumbs = reactive([
      {
        label: "預約日期",
        url: { name: "choose_date" },
      },
    ]);
    const currentDate = new Date();
    const year = ref(currentDate.getFullYear());
    const month = ref(currentDate.getMonth() + 1);

    const addMonth = () => {
      month.value++;
      if (month.value > 12) {
        month.value = 1;
        year.value++;
      }
    };

    const minusMonth = () => {
      month.value--;
      if (month.value < 1) {
        month.value = 12;
        year.value--;
      }
    };

    const postRegisterFunc = () => {
      postRegisterAPI({
        name: '張洛慈',
        email: 'aaa@gmail.com',
        password: 'aaa123',
      })
        .then((res) => console.log(res))
        .catch((err) => console.log(err));
    };

    

    const getList = () => {
      getListAPI({ gid: 1 })
        .then((res) => console.log(res))
        .catch((err) => console.log(err));
    };

    onMounted(() => {
      getList();
      postRegisterFunc();
    });

    return {
      breadcrumbs,
      year,
      month,
      addMonth,
      minusMonth,
    };
  },
};
</script>

<template>
  <BreadCrumbs :items="breadcrumbs" />
  <!-- <TheCircleProgress /> -->
  <div class="choosedate_page_board">
    <fa
      class="choosedate_page_minusMonth"
      icon="caret-left"
      @click="minusMonth"
    />
    <span>{{ year }}</span> ． <span>{{ month }}</span>
    <fa class="choosedate_page_addMonth" icon="caret-right" @click="addMonth" />
    <Calendar :year="year" :month="month" />
  </div>
</template>

<style scoped lang="scss">
@import "@/assets/_variables.scss";

.choosedate_page_board {
  background-color: white;
  // height: 690px;
  padding: 84px;
  font-size: 24px;
  font-weight: bold;
  color: $primaryMiddle;
  text-align: center;

  .choosedate_page_minusMonth,
  .choosedate_page_addMonth {
    cursor: pointer;
    font-size: 18px;
  }

  @media screen and (max-width: $medium) {
    padding: 84px;
    height: 530px;
    font-size: 20px;
  }

  @media screen and (max-width: $small) {
    padding: 40px;
    height: 400px;
    font-size: 20px;
  }
}
</style>
