class Card:
    """
    Card represents flipable cards for using in classroom environment for memorization
    of education content. Every card had two sides: front which is visible at the beginning
    and rear which is hidden. Cards can be fliped which will switch which side of card is
    visible.
    """

    def __init__(self, front_text, rear_text):
        self._front_text = front_text
        self._rear_text = rear_text
        self._visible_text = self._front_text

    @property
    def front_text(self) -> str:
        return self._front_text
    
    @front_text.setter
    def front_text(self, value: str) -> None:
        self._front_text = value

    @property
    def rear_text(self) -> str:
        return self._rear_text
    
    @rear_text.setter
    def rear_text(self, value: str) -> None:
        self._rear_text = value

    @property
    def visible_text(self) -> str:
        return self._visible_text
    
    @visible_text.setter
    def visible_text(self, value: str) -> None:
        self._visible_text = value

    def turn_card(self) -> None:
        """
        Method for fliping visible side of card.
        """
        if self._visible_text == self._front_text:
            self._visible_text = self._rear_text
        else:
            self._visible_text = self._front_text