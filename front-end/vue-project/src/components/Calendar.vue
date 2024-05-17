<script>
import TheCircleProgress from "../components/TheCircleProgress.vue";
import TheCircleBlank from "../components/TheCircleBlank.vue";
import { ref, computed, watchEffect } from "vue";
export default {
  components: {
    TheCircleProgress,
    TheCircleBlank,
  },
  props: {
    year: {
      type: String,
      default: () => new Date().getFullYear().toString(),
    },
    month: {
      type: String,
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

    // 找出當月所有開放日期、開放設置為true，組成陣列，並跳過星期日
    const getDatesInMonth = (year, month) => {
      const today = new Date();
      const twoWeeksLater = new Date(
        today.getTime() + 13 * 24 * 60 * 60 * 1000
      );
      const startDate = new Date(year, month - 1, 1);
      const endDate = new Date(year, month, 0);
      const datesArray = [];

      for (
        let date = new Date(startDate);
        date <= endDate;
        date.setDate(date.getDate() + 1)
      ) {
        console.log("date", date);
        console.log("startDate", startDate);

        // if (date.getDay() === 0) continue;

        const formattedDate = date
          .toLocaleDateString("en-US", {
            year: "numeric",
            month: "2-digit",
            day: "2-digit",
          })
          .replace(/\//g, "-");

        date.setHours(0, 0, 0, 0);
        today.setHours(0, 0, 0, 0);
        twoWeeksLater.setHours(0, 0, 0, 0);

        const isOpen = date >= today && date <= twoWeeksLater;

        datesArray.push({ date: formattedDate, open: isOpen });
      }

      return datesArray;
    };

    watchEffect(() => {
      datesArray.value = getDatesInMonth(props.year, props.month);
    });

    // console.log(datesArray);

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
        <div class="calendar_circle_container" v-if="data.open" :key="'day' + index">
          <div class="calendar_circle_progress">
            <TheCircleProgress :day="index + 1" />
          </div>
        </div>
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
