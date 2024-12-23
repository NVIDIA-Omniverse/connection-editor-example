
# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

import omni.ui as ui
import omni.usd

from .model import AttributeItem, AttributeModel


class AttributeDelegate(ui.AbstractItemDelegate):
    def build_widget(self, model: AttributeModel, item: AttributeItem, column_id: int, level: int, expanded: bool) -> None:
        image_size = 16
        connections = item.attribute.GetConnections()
        tooltips = f"{len(connections)} Connection(s):\n" + "\n".join([str(connection) for connection in connections]) if connections else ""

        with ui.HStack(spacing=2, tooltip=tooltips):
            if connections:
                # Icon to indicate has connections
                with ui.VStack(width=image_size):
                    ui.Spacer()
                    ui.ImageWithProvider(style_type_name_override="TreeView.Connection", width=image_size, height=image_size)
                    ui.Spacer()
            else:
                # No connections, show spacer for alignment
                ui.Spacer(width=image_size)

            ui.Label(item.name, style_type_name_override="TreeView.Item")


class AttributeView:
    def __init__(self):
        self._path = ""
        self._model = AttributeModel()
        self._delegate = AttributeDelegate()
        self._build_ui()

    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, new_path) -> None:
        self._path = new_path
        self._model.path = new_path
        self._path_field.model.set_value(self._path)

    def _build_ui(self) -> None:
        with ui.Frame(accept_drop_fn=self.__accept_drop, drop_fn=self.__drop):
            with ui.VStack(spacing=10):
                with ui.HStack(spacing=15, height=0):
                    ui.Label("Prim Path", width=0)
                    self._path_field = ui.StringField(accept_drop_fn=self.__accept_drop, drop_fn=self.__drop)
                    self._path_field.model.set_value(self._path)
                with ui.ScrollingFrame(style_type_name_override="TreeView.ScrollingFrame"):
                    ui.TreeView(self._model, delegate=self._delegate, root_visible=False, header_visible=False, drop_between_items=True)

    def __accept_drop(self, url: str) -> bool:
        # Here to accept dropping from stage window
        usd_context = omni.usd.get_context()
        stage = usd_context.get_stage()
        prim = stage.GetPrimAtPath(url)
        return True if prim else False

    def __drop(self, url: str) -> None:
        self.path = str(url)
