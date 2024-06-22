export const validateForm = (type, userData, errors) => {
  clearErrorsMsg(errors);
  let isValid = true;

  if (!type && !userData.name) {
    errors.name = "姓名不能為空";
    isValid = false;
  }
  if (!userData.email) {
    errors.email = "Email不能為空";
    isValid = false;
  } else if (!validateEmail(userData.email)) {
    errors.email = "Email格式不正確";
    isValid = false;
  }
  if (!userData.password) {
    errors.password = "密碼不能為空";
    isValid = false;
  }

  return isValid;
};

export const validateEmail = (email) => {
  const re = /\S+@\S+\.\S+/;
  return re.test(email);
};

export const clearErrorsMsg = (errors) => {
  errors.name = "";
  errors.email = "";
  errors.password = "";
};
