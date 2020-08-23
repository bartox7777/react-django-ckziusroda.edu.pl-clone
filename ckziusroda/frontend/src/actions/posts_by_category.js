import axios from "axios";

import { GET_POSTS_BY_CATEGORY } from "./types";

export const getPostsByCategory = (category_slug) => (dispatch) => {
  axios
    .get(`/api/posts/${category_slug}/`)
    .then((res) => {
      if (res.data.length > 0) {
        dispatch({
          type: GET_POSTS_BY_CATEGORY,
          payload: res.data,
        });
      } else {
        dispatch({
          type: GET_POSTS_BY_CATEGORY,
          payload: "NO_RESULTS",
        });
      }
    })
    .catch((err) => {
      console.log(err);
    });
};
