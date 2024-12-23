
# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

import omni.ext
import omni.kit.menu.utils
import omni.ui as ui

from .window import AttributeConnectionWindow

WINDOW_MENU_ROOT = "Window"


class UsdConnectExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        """Run once on startup of the extension."""
        self._window = None
        ui.Workspace.set_show_window_fn(AttributeConnectionWindow.WINDOW_TITLE, self._show_window)
        self._register_menuitem()

    def on_shutdown(self):
        """Run once as the extension shuts down."""
        omni.kit.menu.utils.remove_menu_items(self._menu_entry, name=WINDOW_MENU_ROOT)
        ui.Workspace.set_show_window_fn(AttributeConnectionWindow.WINDOW_TITLE, None)

        if self._window is not None:
            self._window.destroy()
            self._window = None

    def _show_window(self, visible: bool) -> None:
        if visible:
            if self._window is None:
                self._window = AttributeConnectionWindow()
                self._window.set_visibility_changed_fn(self._on_visibility_changed)
            else:
                self._window.visible = True
        else:
            self._window.visible = False

    def _toggle_window(self) -> None:
        self._show_window(not self._is_visible())

    def _register_menuitem(self) -> None:
        self._menu_entry = [
            omni.kit.menu.utils.MenuItemDescription(
                name=AttributeConnectionWindow.WINDOW_TITLE,
                ticked=True,
                ticked_fn=self._is_visible,
                onclick_fn=self._toggle_window,
            )
        ]
        omni.kit.menu.utils.add_menu_items(self._menu_entry, WINDOW_MENU_ROOT)

    def _is_visible(self) -> bool:
        return self._window.visible if self._window else False

    def _on_visibility_changed(self, visible: bool) -> None:
        omni.kit.menu.utils.refresh_menu_items(WINDOW_MENU_ROOT)
