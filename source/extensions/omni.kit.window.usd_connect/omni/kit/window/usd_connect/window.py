
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

from .style import WINDOW_STYLE
from .view import AttributeView


class AttributeConnectionWindow(ui.Window):
    WINDOW_TITLE = "Attribute Connection"

    def __init__(self):
        super().__init__(self.WINDOW_TITLE, width=1000, height=600)

        self.frame.set_build_fn(self._build_ui)
        self.frame.set_style(WINDOW_STYLE)

    def _build_ui(self) -> None:
        with self.frame:
            with ui.HStack(spacing=15):
                with ui.ScrollingFrame():
                    AttributeView()
                with ui.ScrollingFrame():
                    AttributeView()
