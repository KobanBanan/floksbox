export const catalogMenuItems = [
  {
    name: 'Четырехклапанные<br>коробки',
    description: 'для транспортировки и хранения',
    iconOn: '/assets/menu/for_on.png',
    iconOff: '/assets/menu/for_off.png',
    route: '/category/four-flap-boxes',
  },
  {
    name: 'Гофролисты<br>',
    description: 'для упаковки любой сложности',
    iconOn: '/assets/menu/blk_on.png',
    iconOff: '/assets/menu/blk_off.png',
    route: '/category/corrugated-sheets',
  },
  {
    name: 'Сложная высечка<br>',
    description: 'под форму и задачи продукта',
    iconOn: '/assets/menu/clp_on.png',
    iconOff: '/assets/menu/clp_off.png',
    route: '/category/complex-cutting',
  },
  {
    name: 'Офсетная печать<br>',
    description: 'яркая стойкая печать на упаковке',
    iconOn: '/assets/menu/plg_on.png',
    iconOff: '/assets/menu/plg_off.png',
    route: '/category/offset-printing',
  },
  {
    name: 'Подарочные<br>пакеты',
    description: 'для розницы и подарков',
    iconOn: '/assets/menu/pkt_on.png',
    iconOff: '/assets/menu/pkt_off.png',
    route: '/category/gift-bags',
  },
  {
    name: 'Шляпные&nbsp;коробки<br>',
    description: 'для цветов и премиальных товаров',
    iconOn: '/assets/menu/rnd_on.png',
    iconOff: '/assets/menu/rnd_off.png',
    route: '/category/hat-boxes',
  },
  {
    name: 'Дизайнерская<br>упаковка',
    description: 'под задачи вашего бренда',
    iconOn: '/assets/menu/dsg_on.png',
    iconOff: '/assets/menu/dsg_off.png',
    route: '/category/designer-packaging',
  },
  {
    name: 'Кашированная<br>гофроупаковка',
    description: 'прочность и премиальный вид',
    iconOn: '/assets/menu/klp_on.png',
    iconOff: '/assets/menu/klp_off.png',
    route: '/category/laminated-corrugated',
  },
  {
    name: 'Гофроупаковка<br>с флексопечатью',
    description: 'для больших тиражей и брендинга',
    iconOn: '/assets/menu/dvj_on.png',
    iconOff: '/assets/menu/dvj_off.png',
    route: '/category/flexo-corrugated',
  },
  {
    name: 'FEFCO',
    description: 'поиск по каталогу FEFCO',
    iconOn: '/assets/fefco/icons/0100.svg',
    iconOff: '/assets/fefco/icons/0100.svg',
    route: '/fefco',
    iconSvg: true,
  },
]

export function useCatalogMenuItems() {
  const plainCatalogLabel = (htmlText) => htmlText.replace(/<br\s*\/?>/gi, ' ').replace(/&nbsp;/g, ' ')

  return {
    catalogMenuItems,
    plainCatalogLabel,
  }
}
