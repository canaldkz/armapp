let rus_locale = {
  cancel: 'Отмена',
  clear: 'Очистить',
  done: 'ОК',
  months: [
    'Январь',
    'Февраль',
    'Март',
    'Апрель',
    'Май',
    'Июнь',
    'Июль',
    'Август',
    'Сентябрь',
    'Октябрь',
    'Ноябрь',
    'Декабрь',
  ],
  monthsShort: [
    'Янв',
    'Фев',
    'Мар',
    'Апр',
    'Май',
    'Июн',
    'Июл',
    'Авг',
    'Сен',
    'Окт',
    'Ноя',
    'Дек',
  ],
  weekdaysShort: [
    'Понедельник',
    'Вторниик',
    'Среда',
    'Четверг',
    'Пятница',
    'Суббота',
    'Воскресенье',
  ],
  weekdaysAbbrev: [
    'Пн',
    'Вт',
    'Ср',
    'Чт',
    'Пт',
    'Сб',
    'Вс',
  ],
}

document.addEventListener('DOMContentLoaded', function () {
  let datepick = M.Datepicker.init(document.querySelector('.datepicker'), {
    format: 'dd.mm.yyyy',
    i18n: rus_locale,
  })
})
