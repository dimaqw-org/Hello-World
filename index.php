<?php declare(strict_types = 1);

class HelloWorld
{
        public function sayHello(DateTimeImutable $date): void
        {
                echo 'Hello, 7' . $date->format('j. n. Y');
        }
}



