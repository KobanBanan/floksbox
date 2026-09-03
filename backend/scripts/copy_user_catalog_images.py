"""Copy user-provided catalog images into project data folders."""
from __future__ import annotations

import shutil
from pathlib import Path

ASSETS = Path(
    r"C:\Users\lizal\.cursor\projects\c-Users-lizal-Documents-floksbox-main\assets"
)
ROOT = Path(__file__).resolve().parents[1]

# Prefer newest upload per prefix (longer hash suffix = user batch from chat)
USER_FILES = {
    "paket_01": "c__Users_lizal_AppData_Roaming_Cursor_User_workspaceStorage_13e56adad1369fcb81bfa40a72e5891a_images_paket_01-269512f8-41f3-481a-bb38-2d96f101a905.png",
    "paket_02": "c__Users_lizal_AppData_Roaming_Cursor_User_workspaceStorage_13e56adad1369fcb81bfa40a72e5891a_images_paket_02-f989a1ed-9705-4c4b-87b4-34694e2d3f10.png",
    "paket_03": "c__Users_lizal_AppData_Roaming_Cursor_User_workspaceStorage_13e56adad1369fcb81bfa40a72e5891a_images_paket_03-64a91f63-0049-405f-b906-30e3b0c1a6f4.png",
    "paket_04": "c__Users_lizal_AppData_Roaming_Cursor_User_workspaceStorage_13e56adad1369fcb81bfa40a72e5891a_images_paket_04-17832a85-57b9-46e1-98b5-af309ee05bfb.png",
    "paket_05": "c__Users_lizal_AppData_Roaming_Cursor_User_workspaceStorage_13e56adad1369fcb81bfa40a72e5891a_images_paket_05-e9adf46b-fb67-48a0-b47d-949b314c9021.png",
    "paket_06": "c__Users_lizal_AppData_Roaming_Cursor_User_workspaceStorage_13e56adad1369fcb81bfa40a72e5891a_images_paket_06-4a4e4fdc-dfd1-4b81-ac69-3515dc3ca7de.png",
    "paket_07": "c__Users_lizal_AppData_Roaming_Cursor_User_workspaceStorage_13e56adad1369fcb81bfa40a72e5891a_images_paket_07-6c0bc0ff-2356-4462-aa7f-8ef464d177b4.png",
    "paket_08": "c__Users_lizal_AppData_Roaming_Cursor_User_workspaceStorage_13e56adad1369fcb81bfa40a72e5891a_images_paket_08-f2035fce-81b2-4274-ada2-99373e9c6cd6.png",
    "quadpack_01": "c__Users_lizal_AppData_Roaming_Cursor_User_workspaceStorage_13e56adad1369fcb81bfa40a72e5891a_images_quadpack_01-af2bcca4-1bcc-4d07-87ad-db7b8622fb2a.png",
    "quadpack_02": "c__Users_lizal_AppData_Roaming_Cursor_User_workspaceStorage_13e56adad1369fcb81bfa40a72e5891a_images_quadpack_02-6ec69e39-4fb1-4baf-a0ff-9a2ab8159f0d.png",
    "quadpack_03": "c__Users_lizal_AppData_Roaming_Cursor_User_workspaceStorage_13e56adad1369fcb81bfa40a72e5891a_images_quadpack_03-ec9fed82-816e-4715-808e-c6ec44c35329.png",
    "quadpack_04": "c__Users_lizal_AppData_Roaming_Cursor_User_workspaceStorage_13e56adad1369fcb81bfa40a72e5891a_images_quadpack_04-b6a8974c-0de6-43fb-8536-10e8640e990a.png",
    "quadpack_05": "c__Users_lizal_AppData_Roaming_Cursor_User_workspaceStorage_13e56adad1369fcb81bfa40a72e5891a_images_quadpack_05-9892a66c-4415-4648-8b9f-08a3614b2db4.png",
    "quadpack_06": "c__Users_lizal_AppData_Roaming_Cursor_User_workspaceStorage_13e56adad1369fcb81bfa40a72e5891a_images_quadpack_06-d3133034-9f6a-4466-b784-d7f00b84123e.png",
    "quadpack_07": "c__Users_lizal_AppData_Roaming_Cursor_User_workspaceStorage_13e56adad1369fcb81bfa40a72e5891a_images_quadpack_07-06b81f2b-f67a-4fd2-aa5f-e69a5c80e469.png",
    "pr1": "c__Users_lizal_AppData_Roaming_Cursor_User_workspaceStorage_13e56adad1369fcb81bfa40a72e5891a_images_pr1-62ce2cbb-f6f6-48c0-9313-c13500586338.png",
    "pr2": "c__Users_lizal_AppData_Roaming_Cursor_User_workspaceStorage_13e56adad1369fcb81bfa40a72e5891a_images_pr2-8058f9bc-2c91-41d9-817a-f24f420bea98.png",
}

GIFT_BAG_NAMES = [
    "Крафт-пакет с бумажными шнурами",
    "Ламинированный пакет с бумажными шнурами",
    "Пакет на лентах",
    "Крафт-мешок на затяжке",
    "Ламинированный пакет с полноцветной печатью",
    "Крафт-пакет с тиснением",
    "Крафт-пакет с крафтовыми ручками",
    "Белый пакет с крафтовыми ручками",
]

QUADPACK_NAMES = [
    "Бурые четырехклапанные короба",
    "Четырехклапанные короба из гофрокартона с ручками",
    "Белые короба из гофрокартона",
    "Четырехклапанные короба из гофрокартона с вентиляционными отверстиями",
    "Четырехклапанные короба из гофрокартона-тубусы",
    "Четырехклапанные короба с нанесением флексопечати",
]

PUBLIC_NAMES = [
    "01-kraft-bag-paper-cords.png",
    "02-laminated-bag-paper-cords.png",
    "03-bag-ribbon-handles.png",
    "04-kraft-drawstring-pouch.png",
    "05-laminated-fullcolor-bag.png",
    "06-kraft-bag-embossing.png",
    "07-kraft-bag-kraft-handles.png",
    "08-white-bag-kraft-handles.png",
]


def copy_asset(key: str, dest: Path) -> None:
    src = ASSETS / USER_FILES[key]
    if not src.is_file():
        raise FileNotFoundError(src)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    print(f"copied {key} -> {dest}")


def main() -> None:
    gift_dir = ROOT / "data" / "gift_bags"
    quad_dir = ROOT / "data" / "quadpack"
    flexo_dir = ROOT / "data" / "flexo"
    laminated_dir = ROOT / "data" / "laminated"
    public_dir = ROOT / ".." / "frontend" / "public" / "catalog" / "gift-bags"
    public_dir = public_dir.resolve()

    for i in range(1, 9):
        key = f"paket_{i:02d}"
        copy_asset(key, gift_dir / f"gift_bag_{i:02d}.png")
        copy_asset(key, public_dir / PUBLIC_NAMES[i - 1])

    for i in range(1, 7):
        key = f"quadpack_{i:02d}"
        copy_asset(key, quad_dir / f"quadpack_{i:02d}.png")

    copy_asset("quadpack_07", laminated_dir / "laminated_01.png")
    copy_asset("quadpack_07", quad_dir / "quadpack_07.png")
    copy_asset("pr1", flexo_dir / "flexo_01.png")
    copy_asset("pr1", flexo_dir / "offset_unfold.png")
    copy_asset("pr2", quad_dir / "pr2_unfold.png")


if __name__ == "__main__":
    main()
