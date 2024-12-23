
# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

from pathlib import Path

import omni.ui as ui

CURRENT_PATH = Path(__file__).parent
DATA_PATH = CURRENT_PATH.parent.parent.parent.parent.joinpath("data")

WINDOW_STYLE = {
    "TreeView.ScrollingFrame": {"background_color": 0xFF23211F},
    "TreeView": {
        "background_color": 0xFF23211F,
        "background_selected_color": 0x664F4D43,
        "secondary_color": 0xFF403B3B,
        "border_width": 1.5,
    },
    "TreeView.Connection": {"image_url": f"{DATA_PATH}/Expression.svg"},
    "TreeView.Item": {"font_size": 16, "margin": 2, "color": 0xFF8A8777},
    "TreeView.Item:hovered": {"color": 0xFFBBBAAA},
    "TreeView.Item:selected": {"color": 0xFFDDDCCC},
}