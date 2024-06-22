<script>
import TheCircleProgress from "../components/TheCircleProgress.vue";
import TheCircleBlank from "../components/TheCircleBlank.vue";
import getDatesInMonth from "@/utils/getDatesInMonth";
import { ref, computed, watchEffect } from "vue";
export default {
  components: {
    TheCircleProgress,
    TheCircleBlank,
  },
  props: {
    year: {
      type: Number,
      default: () => new Date().getFullYear().toString(),
    },
    month: {
      type: Number,
      default: () => (new Date().getMonth() + 1).toString(), // 預設為當前月份
    },
  },
  setup(props) {
    const weekdays = ref(["日", "一", "二", "三", "四", "五", "六"]);
    const datesArray = ref([]);

    // 計算當月第一天是星期幾
    const firstDayOfWeek = computed(() => {
      return new Date(props.year, props.month - 1, 1).getDay();
    });


    watchEffect(() => {
      datesArray.value = getDatesInMonth(props.year, props.month);
    });

    return {
      weekdays,
      firstDayOfWeek,
      datesArray,
    };
  },
};
</script>

<template>
  <div class="calendar">
    <div class="calendar_weekdays">
      <div class="calendar_weekday" v-for="day in weekdays" :key="day">{{ day }}</div>
    </div>
    <div class="calendar_days">
      <div class="calendar_blank" v-for="blank in firstDayOfWeek"></div>

      <template v-for="(data, index) in datesArray">
        <!-- 開放日 -->
        <div class="calendar_circle_container" v-if="data.open" :key="'day' + index">
          <div class="calendar_circle_progress">
            <TheCircleProgress :day="index + 1" />
          </div>
        </div>
        <!-- 關閉日 -->
        <div class="calendar_blank_container" v-else :key="'blank-circle' + index">
          <div class="calendar_circle_progress">
            <TheCircleBlank :day="index + 1" />
          </div>
        </div>
      </template>
    </div>
  </div>
</template>

<style scoped lang="scss">
@import "@/assets/_variables.scss";

.calendar_weekdays {
  display: flex;
  justify-content: space-between;
  margin-top: 40px;
  .calendar_weekday {
    text-align: center;
    width: calc(100% / 7);
  }

  @media screen and (max-width: $medium) {
    margin-top: 30px;
  }

  @media screen and (max-width: $small) {
    margin-top: 20px;
  }
}

.calendar_days {
  margin-top: 10px;
  display: grid;
  text-align: center;
  grid-template-columns: repeat(7, 1fr);
  .calendar_blank,
  .calendar_circle_container,
  .calendar_blank_container {
    margin-top: 20px;
  }
  .calendar_circle_progress {
    display: flex;
    justify-content: center;
  }
}
</style>
