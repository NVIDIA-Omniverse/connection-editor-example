
# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

from typing import List, Optional

import omni.ui as ui
import omni.usd
from pxr import Sdf


class AttributeItem(ui.AbstractItem):
    def __init__(self, attribute):
        self.attribute = attribute
        self.name = self.attribute.GetName()
        super().__init__()


class AttributeModel(ui.AbstractItemModel):
    def __init__(self, path: str = None):
        self._path = path
        self._items = []
        super().__init__()

    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, new_path: str) -> None:
        self._path = new_path
        self._item_changed(None)

    def get_item_children(self, item: Optional[AttributeItem] = None) -> List[AttributeItem]:
        if item is None and self._path:
            self._items = []
            usd_context = omni.usd.get_context()
            stage = usd_context.get_stage()
            prim = stage.GetPrimAtPath(self._path)
            if prim:
                attributes = prim.GetAttributes()
                for attr in attributes:
                    self._items.append(AttributeItem(attr))
            return self._items
        return []

    def get_item_value_model_count(self, item: Optional[AttributeItem] = None):
        # Always show 1 column in TreeView
        return 1

    def get_item_value_model(self, item: Optional[AttributeItem], column_id: int) -> ui.SimpleStringModel:
        return ui.SimpleStringModel(item.name)

    """Enable drag and drop"""
    def get_drag_mime_data(self, item: Optional[AttributeItem]) -> str:
        return str(item.attribute.GetPath())

    def drop_accepted(self, target_item: Optional[AttributeItem], source: str, drop_location=-1):
        # Here only accept drop to treeview item to add connection
        return isinstance(source, str) and isinstance(target_item, AttributeItem)

    def drop(self, target_item: Optional[AttributeItem], source: str, drop_location=-1):
        if isinstance(source, str) and isinstance(target_item, AttributeItem):
            target_item.attribute.AddConnection(Sdf.Path(source))
            self._item_changed(target_item)