import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { ContinutFilmService, Film } from 'src/app/servicii/continut-film.service';
import {MatBottomSheet} from '@angular/material/bottom-sheet';
import { SelectorSortare } from './selector/selector-sortare.component';
import { ServiciuSelectorSortareService } from 'src/app/servicii/serviciu-selector-sortare.service';


@Component({
  selector: 'app-paginafilme',
  templateUrl: './paginafilme.component.html',
  styleUrls: ['./paginafilme.component.scss']
})
export class PaginafilmeComponent implements OnInit {
  constructor(private continut:ContinutFilmService, private selectorSortare: MatBottomSheet, private comunicareSelector:ServiciuSelectorSortareService) {
    this.comunicareSelector.comunicare.subscribe(value => {
      if (value) {
        switch(value){
          case 1:
            this.filme.sort((n1,n2) => (n1.nume > n2.nume ? 1 : -1));
            break;
          case 2:
            this.filme.sort((n1,n2) => (n1.regizor > n2.regizor ? 1 : -1));
            break;
          case 3:
            this.filme.sort((n1,n2) => n1.an - n2.an);
            break;
          case 4:
            this.filme.sort((n1,n2) => n2.an - n1.an);
            break;
          case 5:
            this.filme.sort((n1,n2) => 0 - (n1.nume > n2.nume ? 1 : -1));
            break;
          case 6:
            this.filme.sort((n1,n2) => 0 - (n1.regizor > n2.regizor ? 1 : -1));
            break;
          case 7:
            this.filme.sort((n1,n2) => n1.durata - n2.durata);
            break;
          case 8:
            this.filme.sort((n1,n2) => n2.durata - n1.durata);
            break;
        }
      }
    });
   }


  salveazaReview(){
    this.continut.salveazaReview();
  }
  filme!:Film[];
  campCautare = new FormControl();

  ngOnInit(): void {
    this.filme = this.continut.getContinutFilm();
  }

  cautare(){
    this.filme = this.continut.getContinutFilm();
    var filmeFiltrate:Film[] = [];
    this.filme.forEach(element => {
      if(element.an == this.campCautare.value || element.nume.includes(this.campCautare.value) || element.regizor.includes(this.campCautare.value) || element.descriere.includes(this.campCautare.value)){
        filmeFiltrate.push(element);
      }
    });
    this.filme = filmeFiltrate;
  }

  afisareMeniuSortare(){
    this.selectorSortare.open(SelectorSortare);
  }
  //deleteReview(){
   // this.continut.deleteReview();
  //}
}
