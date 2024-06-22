import { usePermission } from "@/utils/permission";
import { getCurrentInstance } from "vue";
import Cookies from "js-cookie";

export default {
  mounted(el, binding, vnode) {
    const { hasPermission } = usePermission();

    let btnPermissionsArr = [];
    const permissions = Cookies.get("permissions");

    if (binding.value) {
      //有給參數: v-has="['admin', 'editor']"
      btnPermissionsArr = Array.isArray(binding.value)
        ? binding.value
        : [binding.value];
    } else {
    
      let permissionsArr = permissions.split(",");
      btnPermissionsArr = permissionsArr;
    }

    // console.log(hasPermission(btnPermissionsArr));
    if (hasPermission(btnPermissionsArr) !== true) {
      el.parentNode && el.parentNode.removeChild(el);
    }
  },
};
