# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the 'License'); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals, absolute_import

import unittest

from linebot.models import (
    FlexSendMessage,
    BlockStyle,
    BubbleStyle,
    BubbleContainer,
    CarouselContainer,
    BoxComponent,
    TextComponent,
    SeparatorComponent,
    ImageComponent,
    ButtonComponent,
    FillerComponent,
    IconComponent,
    SpacerComponent,
    URIAction,
)
from tests.models.serialize_test_case import SerializeTestCase


class TestFlexMessage(SerializeTestCase):
    def test_flex_message(self):
        arg = {
            'alt_text': 'this is a flex message',
            'contents':
                BubbleContainer(
                    body=BoxComponent(
                        layout='vertical',
                        contents=[
                            TextComponent(text='hello', wrap=True, maxLines=1),
                            TextComponent(text='world')
                        ]
                    )
                )
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.FLEX),
            FlexSendMessage(**arg).as_json_dict()
        )

    def test_bubble_container(self):
        arg = {
            'header':
                BoxComponent(layout='vertical',
                             contents=[TextComponent(text='Header text')]),
            'hero':
                ImageComponent(uri='https://example.com/flex/images/image.jpg'),
            'body':
                BoxComponent(layout='vertical',
                             contents=[TextComponent(text='Body text')]),
            'footer':
                BoxComponent(layout='vertical',
                             contents=[TextComponent(text='Footer text')]),
            'styles':
                BubbleStyle(
                    header=BlockStyle(background_color='#00ffff'),
                    hero=BlockStyle(background_color='#00ffff',
                                    separator=True),
                    footer=BlockStyle(background_color='#00ffff',
                                      separator=True,
                                      separator_color='#00ffff')
                )
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.BUBBLE),
            BubbleContainer(**arg).as_json_dict()
        )

    def test_bubble_style(self):
        arg = {
            'header':
                BlockStyle(background_color='#00ffff'),
            'hero':
                BlockStyle(background_color='#00ffff',
                           separator=True),
            'footer':
                BlockStyle(background_color='#00ffff',
                           separator=True,
                           separator_color='#00ffff')
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            BubbleStyle(**arg).as_json_dict()
        )

    def test_block_style(self):
        arg = {
            'background_color': '#00ffff',
            'separator': True,
            'separator_color': '#000000'
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            BlockStyle(**arg).as_json_dict()
        )

    def test_carousel_container(self):
        arg = {
            'contents': [
                BubbleContainer(
                    body=BoxComponent(
                        layout='vertical',
                        contents=[TextComponent(text='Hey')]
                    )
                ),
                BubbleContainer(
                    body=BoxComponent(
                        layout='vertical',
                        contents=[TextComponent(text='Foo')]
                    )
                ),
            ]
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.CAROUSEL),
            CarouselContainer(**arg).as_json_dict()
        )

    def test_box_component(self):
        arg = {
            'layout': 'vertical',
            'contents': [
                ImageComponent(url='https://example.com/flex/images/image.jpg'),
                SeparatorComponent(),
                TextComponent(text='Text in the box'),
            ]
        }

        self.assertEqual(
            self.serialize_as_dict(arg, type=self.BOX),
            BoxComponent(**arg).as_json_dict()
        )

    def test_button_component(self):
        arg = {
            'action':
                URIAction(label='Tap me',
                          uri='https://example.com'),
            'style': 'primary',
            'color': '#0000ff'
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.BUTTON),
            ButtonComponent(**arg).as_json_dict()
        )

    def test_filler_component(self):
        arg = {}
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.FILLER),
            FillerComponent(**arg).as_json_dict()
        )

    def test_icon_component(self):
        arg = {
            'url': 'https://example.com/icon/png/caution.png',
            'size': 'lg',
            'aspect_ratio': '1.91:1'
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.ICON),
            IconComponent(**arg).as_json_dict()
        )

    def test_image_component(self):
        arg = {
            'url': 'https://example.com/flex/images/image.jpg',
            'size': 'full',
            'aspect_ratio': '1.91:1'
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.IMAGE),
            ImageComponent(**arg).as_json_dict()
        )

    def test_separator_component(self):
        arg = {
            'color': '#000000'
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.SEPARATOR),
            SeparatorComponent(**arg).as_json_dict()
        )

    def test_spacer_component(self):
        arg = {
            'size': 'md'
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.SPACER),
            SpacerComponent(**arg).as_json_dict()
        )

    def test_text_component(self):
        arg = {
            'text': 'Hello, World!',
            'size': 'xl',
            'weight': 'bold',
            'color': '#0000ff'
        }
        self.assertEqual(
            self.serialize_as_dict(arg, type=self.TEXT),
            TextComponent(**arg).as_json_dict()
        )


if __name__ == '__main__':
    unittest.main()
