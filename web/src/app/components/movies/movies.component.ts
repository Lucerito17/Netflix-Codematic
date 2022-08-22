import { Component, OnInit } from '@angular/core';
import { MovieService } from 'src/app/services/movie.service';
import { Movie } from '../../components/movies/entities/movie';

@Component({
  selector: 'app-movies',
  templateUrl: './movies.component.html',
  styleUrls: ['./movies.component.scss']
})
export class MoviesComponent implements OnInit {

  movies:Movie[] =[]

  constructor(private service:MovieService) { }


  ngOnInit(): void {
    this.service.getMovies()
    .subscribe(data => {
      this.movies = data;
    })
  }

}
