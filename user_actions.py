from kivy.uix.relativelayout import RelativeLayout


def keyboard_closed(self):
    self.keyboard.unbind(on_key_down=self.on_keyboard_down)
    self.keyboard.unbind(on_key_up=self.on_keyboard_up)
    self.keyboard = None


def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'a':
        self.current_speed_x = self.SPEED_
    elif keycode[1] == 'd':
        self.current_speed_x = -self.SPEED_
    elif keycode[1] == 'left':
        self.current_speed_x = self.SPEED_
    elif keycode[1] == 'right':
        self.current_speed_x = -self.SPEED_


    return True


def on_keyboard_up(self, keyboard, keycode,):
    self.current_speed_x = 0
    return True


def on_touch_down(self, touch):
    # game_over = False
    # game_start = False
    if not self.game_over and self.game_start:
        if touch.x < self.width/2:
            # print("<-")
            self.current_speed_x = self.SPEED_x
        else:
            # print("->")
            self.current_speed_x = -self.SPEED_x
    return super(RelativeLayout, self).on_touch_down(touch)


def on_touch_up(self, touch):
    # print("Up")
    self.current_speed_x = 0
