
# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

import asyncio
from pathlib import Path

import omni.kit.app
import omni.kit.test
import omni.ui as ui
from omni.ui.tests.test_base import OmniUiTest

CURRENT_PATH = Path(__file__).parent
TEST_DATA_PATH = CURRENT_PATH.parent.parent.parent.parent.parent.joinpath("data").joinpath("tests")


class TestWindow(OmniUiTest):
    """Test the window with a simple golden image test."""

    async def setUp(self):
        """Before running each test."""
        await super().setUp()

        self._golden_img_dir = TEST_DATA_PATH.absolute().joinpath("golden_img").absolute()

        ui.Workspace.show_window("Attribute Connection")

    async def tearDown(self):
        """After running each test."""
        await super().tearDown()

    async def test_ui(self):
        """Test a simple window without doing anything after loading."""
        window = ui.Workspace.get_window("Attribute Connection")
        await self.docked_test_window(window=window, width=1280, height=720)

        await self.finalize_test(golden_img_dir=self._golden_img_dir, golden_img_name="test_window.png")
