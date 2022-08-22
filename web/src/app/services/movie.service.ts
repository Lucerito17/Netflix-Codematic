import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Movie } from '../components/movies/entities/movie';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MovieService {

  constructor(private http:HttpClient) {}

  //observable para lista de datos indicados 
  getMovies(): Observable<Movie[]>{
    const url = 'http://127.0.0.1:8000/api/movies/';//https://630238599eb72a839d6b7473.mockapi.io/movies
    const headers = new HttpHeaders({
      'content-type': 'application/json',
      'Autorization': 'Bearer' + 'hiahciadl'
    })

    return this.http
      .get<Movie[]>(url, {headers:headers})
      .pipe()
  }
}
