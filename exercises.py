def is_real_palindrome(input: str) -> bool:
    """
    function isRealPalindrome(str) {
      const cleanedStr = str.replace(/\W/g, '').toUpperCase()
      const halfStrSize = Math.floor(cleanedStr.length/2)
      const reversedFirstHalf = cleanedStr.substr(0, halfStrSize).split('').reverse().join('')

      console.log(reversedFirstHalf)
      console.log(cleanedStr.endsWith(reversedFirstHalf))

      return cleanedStr.endsWith(reversedFirstHalf)
    }
    // isRealPalindrome("Eva, can I see bees in a cave?")
    // isRealPalindrome("123abb321")
    """
    return NotImplemented


def running_total(input_arr: list) -> int:
    """ 
    {
      if (typeof(arr) != 'object' || arr.length < 1){
        console.log(arr)
        return arr
      } 
      const reducer = (acc, curr) => {
        return acc+curr
      }

      const sumArr = arr.map((el, idx, origArr) => {
        return origArr.slice(0,idx+1).reduce(reducer, 0)
      })
      console.log(sumArr)
      return sumArr
    }
    """
    return NotImplemented

def swap(sentence: str) -> str:
    """
    function swap(sentence) {
      if(sentence.length <= 1) {
        console.log(sentence)
        return sentence
      }
      let arrOfWords = sentence.split(" ")

      arrOfWords = arrOfWords.map((word) => {
        wordSplit = word.split('')
        let origFirst = wordSplit[0];
        let origLast = wordSplit[wordSplit.length-1];
        wordSplit[0] = origLast;
        wordSplit[wordSplit.length-1] = origFirst;
        word = wordSplit.join('');
        // console.log(word);
        return word
      })
      console.log(arrOfWords.join(" "))
      return arrOfWords.join(" ")
    }

    // swap('Oh what a wonderful day it is');  // "hO thaw a londerfuw yad ti si"
    // swap('a');                              // "a"
    // swap('Abcde');                          // "ebcdA"
    """
    return NotImplemented

def word_sizes(input_sentence: str) -> dict:
    """
    {
      // declare empty obj {}
      const objMap = {};
      
      if (sentence.length <= 0){
        // console.log({})
        return objMap
      }

      // .split(" ") sentence into arr of str
      const arrOfWords = sentence.split(" ")

      arrOfWords.forEach((word) => {
        let wordLength = word.length;
        if (wordLength in objMap) {
          objMap[wordLength]++;
        } else {
          objMap[wordLength] = 1
        }
        return objMap
      })

      console.log(objMap)
      // return obj
      return objMap

    }

    // wordSizes('Four score and seven.');                       // { "3": 1, "4": 1, "5": 1, "6": 1 }
    // wordSizes('Hey diddle diddle, the cat and the fiddle!');  // { "3": 5, "6": 1, "7": 2 }
    // wordSizes("What's up doc?");                              // { "2": 1, "4": 1, "6": 1 }
    // wordSizes('');                                            // {}
    """
    return NotImplemented

def union(arr1: list, arr2: list) -> list:
    """ 
    {
      const arrConcat = arr1.concat(arr2)

      // refactored code block begins
      return arrConcat.filter((el, idx, arr) => {
        /*
        if (arr.slice(0,idx).includes(el)) {
          return null
        } else {
          return el
        }
        */
      return arr.slice(0, idx).find(int => int === el ) ? null : el
      })
    }
    union([1, 3, 5], [3, 6, 9]);     // [1, 3, 5, 6, 9]
    union([2, 2, 2, 2], [10, 5, 2]); // [2, 10, 5]
    """
    return NotImplemented

def first_recurring(word: str) -> str: 
    """
    {
      const arrOfChcs = word.split("");
      const repeatingChcs = [];
      /*
      arrOfChcs.forEach((chc, idx, arr) => {
        if (arr.slice(idx+1).includes(chc)) {
          repeatingChcs.push(chc)
        } 
      })
      
      console.log(repeatingChcs)
      return repeatingChcs[0] ? repeatingChcs[0] : ""
      */
      
      // refactored using filter and find on Carmen's suggestion
      const repeatChcs = arrOfChcs.filter((chc, idx, arr) => {
        // refactoring my refactored code
        return arr.slice(idx+1).find(el => el === chc)
        /*
        if(arr.slice(idx+1).includes(chc)) {
          arr.slice(idx+1).find(el => el === chc)
          return chc
        }
        */
      })

      return repeatChcs.length > 0 ? repeatChcs[0] : ""
      
      /*
      const recurrenceMap = arrOfChcs.reduce(function (recurrenceList, currChc){
        recurrenceList[currChc] = (recurrenceList[currChc] || 0)+1
        return recurrenceList
      }, new Map())

      console.log(recurrenceMap[Symbol.iterator]())
      */
    }

    firstRecurring('reuben');           // "e"
    firstRecurring('anne');             // "n"
    firstRecurring('restaurant');       // "r"
    firstRecurring('paul');             // ""
    """
    return NotImplemented

def show_multiplicative_average(input: list) -> int: 
    """
    {
      let rawProduct = arr.reduce(function(product, currOperand) {
        return product * currOperand
      })
      
      rawProduct /= arr.length
      rawProduct = rawProduct.toFixed(3).toString()
      console.log(rawProduct)
      return rawProduct

    }

    // showMultiplicativeAverage([3, 5]);                   // "7.500"
    // showMultiplicativeAverage([2, 5, 7, 11, 13, 17]);    // "28361.667"
    """

def multiply_list(arr1: list, arr2: list) -> int:
    """
    {
      const productList = arr1.map((operand, idx) => operand * arr2[idx])
      console.log(productList)
      return productList
    }

    // multiplyList([3, 5, 7], [9, 10, 11]);  // [27, 50, 77]
    // multiplyList([5, 10, 15, 20], [1, 2, 3, 4]);  // [5, 20, 45, 80]
    """
    return NotImplemented

def sequence(num: int) -> list: 
    """
    {
      // accidentally came across this answer from Fabio Antunes on SO when looking for a method that would create a new array of a sequence of integers
      // https://stackoverflow.com/questions/3746725/how-to-create-an-array-containing-1-n

      return Array.from(Array(num), (int, idx) => idx+1)
    }

    // sequence(5);    // [1, 2, 3, 4, 5]
    // sequence(3);    // [1, 2, 3]
    // sequence(1);    // [1]
    """
    return NotImplemented

def word_cap(sentence: str) -> str: 
    """
    {
      const arrOfWords = sentence.split(" ").map((word, idx, sentenceArr) => {
        console.log("before", word)
        word = word[0].toUpperCase() + word.slice(1).toLowerCase()
        console.log("after", word)
        return word
      })

      return arrOfWords.join(" ")
    }

    // wordCap('four score and seven');       // "Four Score And Seven"
    // wordCap('the javaScript language');    // "The Javascript Language"
    // wordCap('this is a "quoted" word');    // 'This Is A "quoted" Word'
    """
    return NotImplemented

def process_release_data(new_releases: list) -> list: 
    """
    {
      const processedReleases = newReleases.filter(release => release.id && release.title).map(release => {return {'id': release.id, 'title': release.title}})

      console.log(processedReleases)

      return processedReleases
    }

    // processReleaseData(newReleases); // [{ id: 70111470, title: 'Die Hard'}, { id: 675465, title: 'Fracture' }];
    """
    return NotImplemented

def octal_to_decimal(number_string: str) -> int: 
    """
    {
      const arrOfDigits = numberString.toString().split("").map((digit, idx) => {
        digit = parseInt(digit) * 8 ** (numberString.toString().length - idx - 1)
        // length - idx -1 to get exponent from index
        return digit
      })

      return arrOfDigits.reduce((prod, curr) => prod+curr)
    }

    // octalToDecimal('1');           // 1
    // octalToDecimal('10');          // 8
    // octalToDecimal('130');         // 88
    // octalToDecimal('17');          // 15
    // octalToDecimal('2047');        // 1063
    // octalToDecimal('11');         // 9
    """
    return NotImplemented

def anagram(word: str, array: list) -> str: 
    """
    {
      if ((typeof(word) == 'string') && (typeof(array) == 'object')){

        const treatedWord = word.split('').sort().join('')

        return array.filter(potential => {
          return treatedWord === potential.split('').sort().join('')
        })
      }
    }

    // anagram('listen', ['enlists', 'google', 'inlets', 'banana']);  // [ "inlets" ]
    // anagram('listen', ['enlist', 'google', 'inlets', 'banana']);   // [ "enlist", "inlets" ]
    """
    return NotImplemented

def triangle(a: int, b: int, c: int) -> str: 
    """
    {
      const angles = [a, b, c].sort()

      function isTriangle(anglesArr){
        return anglesArr.every(angle =>  angle > 0 && angle < 180) && anglesArr.reduce((currSum, currVal) => currSum + currVal) === 180
      }

      if (isTriangle(angles)){
        if (angles.some(angle => angle === 90)) {
          console.log("right")
          return "right"
        } else if (angles.every(angle => angle < 90) ) {
          console.log("acute")
          return "acute"
        } else if (angles.some(angle => angle > 90)) {
          console.log("obtuse")
          return "obtuse"
        } else {
          console.log("how did you get past my checks")
          return "invalid"
        }
      } else {
        console.log("invalid")
        return "invalid"
      }
    }

    // triangle(60, 70, 50);       // "acute"
    // triangle(30, 90, 60);       // "right"
    // triangle(120, 50, 10);      // "obtuse"
    // triangle(0, 90, 90);        // "invalid"
    // triangle(50, 50, 50);       // "invalid"
    """
    return NotImplemented

def friday_the_13ths(year: int) -> int: 
    """
    {
      // I kept this the same

      let fri13Counter = 0

      for (i = 0; i < 12; i++){
        let newDate = new Date(year, i, 13) 
        if (newDate.getDay() == 5) {
          fri13Counter++
        }
      }
      console.log(fri13Counter)
      return fri13Counter
    }

    // fridayThe13ths(1986);      // 1
    // fridayThe13ths(2015);      // 3
    // fridayThe13ths(2017);      // 2
    """
    return NotImplemented

