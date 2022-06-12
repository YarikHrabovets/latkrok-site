function mask(inputName, mask, evt) {
    try {
      const text = document.getElementById(inputName);
      let value = text.value;

      try {
        const e = (evt.which) ? evt.which : event.keyCode;
        if ( e == 46 || e == 8 ) {
          text.value = "";
          return;
        }
      } catch (e1) {}

      const literalPattern=/[0\*]/;
      const numberPattern=/[0-9]/;
      let newValue = "";

      for (let vId = 0, mId = 0 ; mId < mask.length ; ) {
        if (mId >= value.length)
          break;

        if (mask[mId] == '0' && value[vId].match(numberPattern) == null) {
          break;
        }

        while (mask[mId].match(literalPattern) == null) {
          if (value[vId] == mask[mId])
            break;

        newValue += mask[mId++];
      }

      newValue += value[vId++];
      mId++;
    }

    text.value = newValue;
  } catch(e) {}
}